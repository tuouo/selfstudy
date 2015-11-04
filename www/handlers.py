#!/usr/bin/envpython3
# -*- coding: utf-8 -*-
' url handlers'

import re, time, json, logging, hashlib, base64, asyncio
from coroweb import get, post
from models import User, Comment, Blog, next_id

@get('/test')
def index(request):
    logging.info('in index-handlers: url handlers	index')
    users = yield from User.findAll()
    logging.info('in index:User ok.')
    return {
        '__template__': 'test.html',
        'users': users
    }

@get('/')
def index(request):
    story = "The quick brown fox jumps over the lazy dog."
    test1 = "Lorem ipsum dolor sit amet,consectetur adipisicing elit,"
    test2 = "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
    test3 = "Ut enim ad minim veniam,quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."
    test4 = "Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur."
    test5 = "Excepteur sint occaecat cupidatat non proident,sunt in culpa qui officia deserunt mollit anim id est laborum."
    blogs = [
        Blog(id ='1', name = 'Story', summary = story, created_at = time.time() - 12000000),
        Blog(id ='2', name = 'test1', summary = test1, created_at = time.time() - 240000),
        Blog(id ='3', name = 'test2', summary = test2, created_at = time.time() - 3600),
        Blog(id ='4', name = 'test3', summary = test3, created_at = time.time() - 720),
        Blog(id ='5', name = 'test4', summary = test4, created_at = time.time() - 600),
        Blog(id ='6', name = 'test5', summary = test5, created_at = time.time() - 12)
    ]
    return {
        '__template__': 'blogs.html',
        'blogs': blogs
    }

@get('/api/users')
def api_get_user(*, page = '1'):
    #page_index = get_page_index(page)
    #num = yield from User.findNumber('count(id)')
    #p = Page(num, page_index)
    #if num == 0:
    #    return dict(page = p, users=())
    users = yield from User.findAll(orderBy = 'created_at desc')#, limit = (p.offset, p.limit)
    for u in users:
        u.password = '******'
    #return dict(page = p, users = users)
    return dict(user = users)