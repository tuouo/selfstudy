#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from aiohttp import web
from config import configs
from jinja2 import Environment, FileSystemLoader
from datetime import datetime
from coroweb import add_routes, add_static
from handlers import cookie2user, COOKIE_NAME
import logging; logging.basicConfig(level = logging.INFO)
import asyncio, os, json, time
import orm

@asyncio.coroutine
def init(loop):
    logging.info('before create_pool')
    yield from orm.create_pool(loop = loop, **configs.db)
    logging.info('after create_pool\n')
    #yield from orm.create_pool(loop = loop, user = 'root', password = '', database = 'awesome')
    app = web.Application(loop = loop, middlewares = [
        logger_factory, auth_factory, response_factory
    ])
    init_jinja2(app, filters = dict(datetime = datetime_filter))
    add_routes(app, 'handlers')
    add_static(app)
    srv = yield from loop.create_server(app.make_handler(), '127.0.0.1', 9000)
    logging.info('server started at http://127.0.0.1:9000 ...')
    return srv

# factory excute by order
@asyncio.coroutine
def logger_factory(app, handler):
    @asyncio.coroutine
    def logger(request):
        logging.info("\tRequest: %s %s" % (request.method, request.path))
        return (yield from handler(request))
    return logger

@asyncio.coroutine
def auth_factory(app, handler):
    @asyncio.coroutine
    def auth(request):
        logging.info('\tcheck user: %s %s' % (request.method, request.path))
        request.__user__ = None
        cookie_str = request.cookies.get(COOKIE_NAME)
        logging.info('\tcookie_str: %s' % cookie_str)
        if cookie_str:
            user = yield from cookie2user(cookie_str)
            if user:
                logging.info('set current user: %s' % user.email)
                request.__user__ = user
        if request.path.startswith('/manage/') and (request.__user__ is None or not request.__user__.admin):
            return web.HTTPFound('/signin')
        return (yield from handler(request))
    return auth

@asyncio.coroutine
def response_factory(app, handler):
    @asyncio.coroutine
    def response(request):
        logging.info("\tResponse handle...%s..." % request)
        r = yield from handler(request)
        logging.info('response_factory: get handlers response OK here')
        logging.info('type(response): %s' % type(r))
        if isinstance(r, web.StreamResponse):
            return r
        if isinstance(r, bytes):
            resp = web.Response(body = r)
            resp.content_type = 'application/octet-stream'
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
                r['__user__'] = request.__user__
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
    logging.info("*********************response ok*********************")
    return response

@asyncio.coroutine
def data_factory(app,handler):
    @asyncio.coroutine
    def parse_data(request):
        if request.method == "POST":
            if request.content_type.startswith('application/json'):
                request.__data__ = yield from request.json()
                logging.info("request json: %s" % str(request.__data__))
            elif request.content_type.startswith('application/x-www-form-urlencoded'):
                request.__data__ = yield from request.post()
                logging.info("request from: %s" % str(request.__data__))
        return (yield from handler(request))
    return parse_data


def init_jinja2(app, **kw):
    logging.info("\tinit jinja2...")
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
    logging.info('jinja2 template path: %s' % path)
    env = Environment(loader=FileSystemLoader(path), **options)
    filters = kw.get('filters', None)
    if filters is not None:
        for name, f in filters.items():
            env.filters[name] = f
    app['__templating__'] = env

def datetime_filter(t):
    delta = int(time.time() - t)
    if delta < 60:
        return '一分钟内'#'In one minute'
    if delta < 3600:
        return '%s 分钟前' % (delta // 60)#'%s minutes ago' % (delta // 60)
    if delta < 86400:
        return '%s 小时前' % (delta // 3600)#'%s hours ago' % (delta // 3600)
    if delta < 604800:
        return '%s 天前' % (delta // 86400)#'%s days ago' % (delta // 86400)
    dt = datetime.fromtimestamp(t)
    return '%s年-%s月-%s日' % (dt.year, dt.month, dt.day)#'%s(Y)-%s(M)-%s(D)' % (dt.year, dt.month, dt.day)


loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()