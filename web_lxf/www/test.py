#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
import orm, asyncio
from models import User, Blog, Comment

def test(loop):
    yield from orm.create_pool(loop = loop, user = 'root', password = '', database = 'awesome')
    u = User(name = 'Test', email = 'test@example.com', password = '1234567890', image = 'about:blank')
    yield from u.save()

loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.close()

# UnKnown output:	Exception ignored in: 