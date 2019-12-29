import cgi
from tornado.web import RequestHandler


class BaseEngineRequestHandler(RequestHandler):
    def prepare(self):
        header = "Content-Type"
        body = "application/json"
        self.set_header(header, body)
        # parse and escape all arguments
        self.parsed_args = {k: cgi.escape(''.join(v)) for k, v in self.request.arguments.iteritems()}

    def on_connection_close(self):
        self.wait_future.cancel()
