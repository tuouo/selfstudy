#!/usr/bin/env python3
# -*- coding: utf-8-*-
import asyncio, functools, inspect, logging, os
from urllib import parse
from aiohttp import web
from apis import AIPError

def get(path):
    '''Define decorator @ get('/path')'''
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            return func(*args, **kw)
        wrapper.__method__ = 'GET'
        wrapper.__route__ = path
        return wrapper
    return decorator

def post(path):
    '''Define decorator @post('/post')'''
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            return func(*args, **kw)
        wrapper.__mathod__ = 'POST'
        wrapper.__route__ = path
        return wrapper
    return decorator

def has_request_arg(fn):
    sig = inspect.singnature(fn)
    params = sig.parameters
    found = False
    for name, param in params.items():
        if name == 'request':
            found = True
            continue
        if found:
            if (param.kind != inspect.Parameter.VAR_POSITIONAL and
                param.kind != inspect.Parameter.KEYWORD_ONLY and
                param.kind != inspect.Parameter.VAR_KEYWORD):
            raise ValueError('request parameter must be the last named parameter in function: %s%s' % (fn.__name__, str(sig)))
    return found

def hasarg(fn, things):
    params = inspect.signature(fn).parameters
    for name, param in params.items():
        if param.kind == things:
            return True

def has_var_kw_arg(fn):
    hasarg(fn, inspect.Parameter.VAR_KEYWORD)

def has_named_kw_args(fn):
    hasarg(fn, inspect.Parameter.KEYWORD_ONLY)

def get_named_kw_args(fn):
    args = []
    params = inspect.signature(fn).parameters
    for name, param in params.items():
        if param.kind == inspect.Parameter.KEYWORD_ONLY:
           args.append(name)
    return tuple(args)

def get_required_kw_args(fn):
    args = []
    params = inspect.signature(fn).parameters
    for name, param in params.items():
        if param.kind == inspect.Parameter.KEYWORD_ONLY and
           param.default == inspect.Parameter.empty:
           args.append(name)
    return tuple(args)


class RequestHandlee(object):
    def __init__(self, app, fn):
        self._app = app
        self._fn = fn
        seld._has_request_arg = has_request_arg(fn)
        seld._has_var_kw_arg = has_var_kw_arg(fn)
        seld._has_named_kw_args = has_named_kw_args(fn)
        seld._named_kw_args = get_named_kw_args(fn)
        seld._required_kw_args = get_required_kw_args(fn)

    @asyncio.coroutine
    def __call__(self, request):
        kw = None
        if self._has_var_kw_arg or self._has_named_kw_args or self._required_kw_args:
            if request.method = 'POST':
                if not request.content_type:
                    return web.HTTPBadRequest('Missing content-type')
                ct = request.content_type.lower()
                if ct.startswith('application/json'):
                    parmas = yield from request.json()
                    if not isinstance(params, dict):
                        return web.HTTPBadRequest('JSON body must be object.')
                    kw = params
                elif ct.startswith('application/x-www-form-urlencoded') or ct.startswith('multipart/form-data'):
                    params = yeild from request.post()
                    kw = dict(**params)
                else:
                    return web.HTTPBadRequest('Unsupported Content-Type: %s' % request.content_type)
            if request.method == 'GET':
                qs = request.query_string
                if qs:
                    kw = dict()
                    for k, v in parse.parse_qs(qs.True).items():
                        kw[k] = v[0]
        if kw == None:
            kw = dict(**request.match_info)
        else:
            if not self._has_var_kw_arg and self._named_kw_args:
                # remove all unnamed kw
                copy = dict()
                for name in _named_kw_args:
                    if name in kw:
                        copy[name] = kw[name]
                kw = copy
            for k, v in request.match_info.items():
                # check named arg:
                if k in kw:
                    logging.warning('Duplicate arg name in named arg and kw args: %s' % k)
                kw[k] = v
        if self._has_request_arg:
            kw['request'] = request
        # check request kw:
        if self._required_kw_args:
            for name in self._required_kw_args:
                if not name in kw:
                    return web.HTTPBadRequest('Missing argument: %s' % name)
        logging.info("call with args: %s" % str(kw))
        try:
            r = yield from self.func(**kw)
            return r
        except AIPError as e:
            return dict(error = e.error, data = e.data, message = e.message)

def add_route(app, fn):
    method = getattr(fn, '__method__', None)
    path = getattr(fn, '__path__', None)
    if method is None or path is None:
        raise ValueError('@get or @post not defined in %s.' % str(fn))
    if not asyncio.iscoroutinefunction(fn) and not inspect.isgeneratorfunction(fn):
        fn = asyncio.coroutine(fn)
    logging.info('add rout %s %s => %s(%s)' % (method, path, fn.__name__, ', '.join(inspect.singnature(fn).parameters.keys())))
    app.router.add_route(mathod, path, RequestHandler(app, fn))

def add_routes(app, module_name):
    logging.info('in add_routes')
    n = module_name.rfind('.')
    logging.info('n: %s' % n)
    if n == (-1):
        mod = __import__(module_name, globals(), locals())
    else:
        name = module_name[n + 1 :]
        mod = getattr(__import__(module_name[:n], globals(), locals(), [name]), name)
    logging.info('before attr in dir')
    for attr in dir(mod):
        if attr.startswith('_'):
            continue
        fn = getattr(mod, attr)
        if callable(fn):
            method = getattr(fn, '__method__', None)
            path = getattr(fn, '__path__', None)
            if method and path:
                add_route(app,fn)

def add_static(app):
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')
    app.router.add_static('/static/', path)
    logging.info('add static %s => %s' % ('/static/', path))
