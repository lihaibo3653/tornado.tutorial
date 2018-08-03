import tornado
import tornado.web
import tornado.ioloop
import settings


class MyFormHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('<html><body><form action="/myform" method="POST">'
                   '<input type="text" name="message">'
                   '<input type="submit" value="Submit">'
                   '</form></body></html>')

    def post(self):
        self.set_header("Content-Type", "text/plain")
        self.write("You wrote " + self.get_body_argument("message"))

class MainHandler(tornado.web.RequestHandler):

    def get(self):
        self.write("Hello, world")



if __name__ == "__main__":

    application = tornado.web.Application([
        (r"/",MainHandler),
        (r"/redirect", tornado.web.RedirectHandler,dict(url='https://github.com'))
    ],**settings.web)
    application.listen(9000, xheaders = True)

    try:
        tornado.ioloop.IOLoop.current().start()
    except (KeyboardInterrupt,BaseException):
        pass