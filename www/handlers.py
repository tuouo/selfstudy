#!/usr/bin/envpython3
# -*- coding: utf-8 -*-
' url handlers'

import re, time, json, logging, hashlib, base64, asyncio
from coroweb import get, post
from models import User, Comment, Blog, next_id

@get('/')
def index(request):
    logging.info('in index-handlers: url handlers	index')
    users = yield from User.findAll()
    logging.info('in index:User ok.')
    return {
        '__template__': 'test.html',
        'users': users
    }