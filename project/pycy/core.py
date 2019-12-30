import cgi
from tornado.web import RequestHandler


class BaseEngineRequestHandler(RequestHandler):
    def prepare(self):
        header = "Content-Type"
        body = "application/json"
        self.set_header(header, body)
        # parse and escape all arguments
        _args = self.request.arguments
        self.parsed_args = {}
        for key in _args:
            v = ''.join([t.decode('utf-') for t in _args[key]])
            self.parsed_args[key] = cgi.escape(v)

    def on_connection_close(self):
        self.wait_future.cancel()
