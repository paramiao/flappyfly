#coding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import os.path
import tornado.auth
import tornado.escape
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.autoreload
import tornado.web
from tornado.options import define, options

import config

#base defines
define(
    "port",
    default=config.default_port, help="run on the given port", type=int
    )


class Application(tornado.web.Application):
    def __init__(self):
        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
        )
        handlers = [
            (r'/cocos2d/(.*)', tornado.web.StaticFileHandler, {'path': settings['static_path']+'/js/cocos2d/'}),
            (r'/src/(.*)', tornado.web.StaticFileHandler, {'path': settings['static_path']+'/js/src/'}),
            (r'/res/(.*)', tornado.web.StaticFileHandler, {'path': settings['static_path']+'/res/'}),
            (r'/(.*?).js', tornado.web.StaticFileHandler, {'path': settings['static_path']+'/js/'}),
            (r"/api_test", APITestHandler),
            (r"/flappy", FlappyHandler),
            (r"/template/(\S+?)/", TemplateTestHandler),
            (r"/async_test", AsyncTestHandler),
        ]
        #you can define base connetions here, such as mongodb, redis.
        self.test_connection = None
        tornado.web.Application.__init__(self, handlers, **settings)


class BaseHandler(tornado.web.RequestHandler):
    @property
    def test_connection(self):
        return self.application.test_connection

    def testFunc(self, argv):
        return argv


#template test
class TemplateTestHandler(BaseHandler):
    def get(self, info):
        self.render('test.html', info=info)

#template test
class FlappyHandler(BaseHandler):
    def get(self):
        self.render('index.html', info=None)


#api test
class APITestHandler(BaseHandler):
    def get(self):
        word = self.get_argument('kw', 'Hello World')
        self.write(word)


#async http request test
class AsyncTestHandler(BaseHandler):
    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def get(self):
        http_client = tornado.httpclient.AsyncHTTPClient()
        response = yield http_client.fetch(
            config.testurl,
            headers={
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_1) \
                AppleWebKit/537.36 (KHTML, like Gecko) \
                Chrome/33.0.1750.58 Safari/537.36'})
        self.write(response.body)


def main():
    tornado.options.parse_command_line()
    application = Application()
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    io_loop = tornado.ioloop.IOLoop.instance()
    tornado.autoreload.start(io_loop)
    io_loop.start()


if __name__ == "__main__":
    main()
