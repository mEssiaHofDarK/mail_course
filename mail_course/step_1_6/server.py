import tornado.web
import tornado.ioloop
import asyncio


class Handler(tornado.web.RequestHandler):

    async def get(self):
        utm_source = self.get_argument('edugram_id')
        print(utm_source)
        self.write(utm_source)
        await self.flush()
        await self.finish()


app = tornado.web.Application([
    (r'/course/matematika-ege', Handler),
])

if __name__ == "__main__":
    app.listen(2222)
    tornado.ioloop.IOLoop.instance().start()
