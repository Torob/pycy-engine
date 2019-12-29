import logging

import tornado
import tornado.web
import tornado.ioloop
import tornado.gen
import tornado.httpclient
from tornado.options import define, options, parse_command_line

from ..app.wall import wall


define("port", default=80, help="run on the given port", type=int)
define("proxy_url", default="http://localhost:81/", help="run on the given port", type=str)
define("debug", default=True, help="run in debug mode")


class ProxyHandler(tornado.web.RequestHandler):
    def initialize(self, proxy_url='/', **kwargs):
        super(ProxyHandler, self).initialize(**kwargs)
        self.proxy_url = proxy_url

    @tornado.gen.coroutine
    def get(self):
        url = self.proxy_url
        if self.request.uri.startswith('/'):
            uri = self.request.uri[1:]
        else:
            uri = self.request.uri

        _block, _response = wall(uri, self)
        if _block:
            self.write(_response)
            return

        req = tornado.httpclient.HTTPRequest(url + uri, headers=self.request.headers)
        client = tornado.httpclient.AsyncHTTPClient()
        response = yield client.fetch(req, raise_error=False)

        self.set_status(response.code)
        if response.code != 200:
            self.finish()
        else:
            if response.body:
                for header in response.headers:
                    if header.lower() == 'content-length':
                        self.set_header(header, str(max(len(response.body), int(response.headers.get(header)))))
                    else:
                        self.set_header(header, response.headers.get(header))

            self.write(response.body)
            self.finish()


def main():
    parse_command_line()
    app = tornado.web.Application()
    handlers = [
        (r"/.*", ProxyHandler, {'proxy_url': options.proxy_url}),
    ]
    app.add_handlers('.*$', handlers)
    logging.critical('Proxy listening on port %s.' % options.port)
    app.listen(options.port)
    try:
        tornado.ioloop.IOLoop.current().start()
    except KeyboardInterrupt:
        logging.critical('Shutting down...')


if __name__ == '__main__':
    main()
