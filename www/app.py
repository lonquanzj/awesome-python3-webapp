import logging; logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time
from datetime import datetime

from aiohttp import web

IP='45.78.52.106'
PORT=9000

def index(request):
    return web.Response(body=b'<h1>Awesome</h1>', content_type='text/html')

@asyncio.coroutine
def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    srv = yield from loop.create_server(app.make_handler(), IP, PORT)
    logging.info('server started at http://%s:%d...'%(IP, PORT))
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
