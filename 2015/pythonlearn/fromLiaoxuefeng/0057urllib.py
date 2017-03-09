#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from urllib import request

reqUrl = request.Request('https://www.douban.com')
reqUrl = request.Request('https://www.baidu.com')
reqUrl.add_header('User-Agent', r'''Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X)
 AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25''')
with request.urlopen(reqUrl) as page:
    date = page.read()
    print("Status:", page.status, page.reason, '\n')
    for k, v in page.getheaders():
        print('%s: %s' %(k, v))
    print("\nDate:", date.decode('utf-8'))
	
	
from urllib import request parse
refer = 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F'
print('Login to weibo.com...')
email = input('Email: ')
passwd = input('Password: ')
login_data = parse.urlencode([
    ('username', email),
    ('password', passwd),
    ('entry', 'mweibo'),
    ('client_id', ''),
    ('savestate', '1'),
    ('ec', ''),
    ('pagerefer', refer)
])

req = request.Request('https://passport.weibo.cn/sso/login')
req.add_header('Origin', 'https://passport.weibo.cn')
req.add_header('User-agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
req.add_header('Referer', refer)

with request.urlopen(req, data = login_data.encode('utf-8')) as page:
    print("Status:", page.status, page.reason, '\n')
    for k, v in page.getheaders():
        print('%s: %s' %(k, v))
    print("\nDate:", page.read().decode('utf-8'))
    