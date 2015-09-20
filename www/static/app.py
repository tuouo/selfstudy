#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging; logging.basicConfig(level = logging.INFO)
import asyncio, os, json, time
from jinja2 import Environment, FileSystemLoader
from datetime import datetime
from aiohttp import web
import orm

@asyncio.coroutine
def init(loop):
    yield from orm.create_pool(loop = loop, user = 'root', password = '', database = 'awesome')
    app = web.Application(loop = loop, middlewares = [
    	logger_factory, response_factory
    ])
    init_jinja2(app, filters = dict(datetime = datetime_filter))
    add_routes(app, 'handlers')
    add_static(app)
    srv = yield from loop.create_server(app.make_handler(), '127.0.0.1', 9000)
    logging.info('server started at http://127.0.0.1:9000 ...')
    return srv

@asyncio.coroutine
def logger_factory(app, handler):
    @asyncio.coroutine
    def logger(request):
        logging.info("Request: %s %s" % (request.method, request.path))
        return (yield from handler(request))
    return logger



def init_jinja2(app, **kw):
    

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()