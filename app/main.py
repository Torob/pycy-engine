import tornado.ioloop
import tornado.locks
import tornado.web
from tornado.options import define, options, parse_command_line

from .urls import url_patterns

define("port", default=8888, help="run on the given port", type=int)
define("debug", default=True, help="run in debug mode")


def main():
    global mod1_instance
    parse_command_line()
    app = tornado.web.Application(url_patterns, debug=options.debug)

    app.listen(options.port)
    print('listening on %s' % options.port)
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()
