#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging; logging.basicConfig(level = logging.INFO)
import asyncio, os, json, time
from jinja2 import Environment, FileSystemLoader
from datetime import datetime
from aiohttp import web
from coroweb import add_routes, add_static
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

@asyncio.coroutine
def response_factory(app, handler):
    @asyncio.coroutine
    def response(request):
        logging.info("Response handle...%s..." % request)
        logging.info("handler: %s" % handler)
        r = yield from handler(request)
        logging.info("r: %s" % r)
        if isinstance(r, web.StreamResponse):
            return r
        if isinstance(r, bytes):
            resp = web.Response(body = r)
            resp.content_type = 'appliaction/octet-stream'
            return resp
        if isinstance(r, str):
            if r.startswith('redirect:'):
                return web.HTTPFound(r[9:])
            resp = web.Response(body = str(r).encode('utf-8'))
            resp.content_type = 'text/html;charset=utf-8'
            return resp
        if isinstance(r, dict):
            template = r.get('__template__')
            if template is None:
                resp = web.Response(body = json.dumps(r, ensure_ascii=False, default=lambda o:o.__dict__).encode('utf-8'))
                resp.content_type = 'application/json;charset=utf-8'
                return resp
            else:
                resp = web.Response(body = app['__templating__'].get_template(template).render(**r).encode('utf-8'))
                resp.content_type = 'text/html;charset=utf-8'
                return resp
        if isinstance(r, int) and r >= 100 and r < 600:		# need check r or anther t
            return web.response(r)
        if isinstance(r, tuple) and len(r) == 2:
            t, m = r
            if isinstance(t, int) and t >= 100 and t < 600:
                 return web.response(t, str(m))
        # default
        logging.info("default...")
        resp = web.Response(body = str(r).encode('utf-8'))
        resp.content_type = 'text/pain;charset=utf-8'
        return resp
    logging.info("response ok...")
    return response


def init_jinja2(app, **kw):
    logging.info("init jinja2...")
    options = dict(
        autoescape = kw.get('autoescape', True),
        block_start_string = kw.get('block_start_string', '{%'),
        block_end_string = kw.get('block_end_string', '%}'),
        variable_start_string = kw.get('variable_start_string', '{{'),
        variable_end_string = kw.get('variable_end_string', '}}'),
        auto_reload = kw.get('auto_reload', True)
    )
    path = kw.get('path',  None)
    if path is None:
        path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
    logging.info('set jinja2 template path: %s' % path)
    env = Environment(loader=FileSystemLoader(path), **options)
    filters = kw.get('filters', None)
    if filters is not None:
        for name, f in filters.items():
            env.filters[name] = f
    app['__templating__'] = env

def datetime_filter(t):
    delta = int(time.time() - t)
    if delta < 60:
        return 'In one minute'
    if delta < 3600:
        return '%s minutes ago' % (delta // 60)
    if delta < 86400:
        return '%s hours ago' % (delta // 3600)
    if delta < 604800:
        return '%s days ago' % (delta // 86400)
    dt = datetime.formatimestamp(t)
    return '%s(Y)-%s(M)-%s(D)' % (dt.year, dt.month, dt.day)


loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()