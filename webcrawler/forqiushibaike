#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from html.parser import HTMLParser
import urllib.request as ur, urllib.error as ue, re
class qiubaiParser(HTMLParser):
    def __init__(self):
        super(qiubaiParser, self).__init__()
        self._tag = ''
        self._Image = False
        self._member = []
        self._all = []

    def handle_starttag(self, tag, attrs):    	
        if ('class', 'thumb') in attrs:
            self._Image = True        
        elif ('class', 'article block untagged mb15') in attrs:
            self._member.append(attrs[1][1])
        elif ('class', 'content') in attrs:
            self._tag = 'content:'
        elif ('class', 'stats-vote') in attrs:
            self._tag = 'vote:'
        elif ('class', 'single-clear') in attrs:
            if not self._Image:
                self._all.append(self._member)
            self._Image = False
            self._member = []
        else:
            for i in attrs:
                if i[0] == "title":
                    for j in attrs:
                        if j[0] == "href":
                            self._member.append(i[1] + j[1])

    def handle_data(self, data):
        if self._tag in ('content:', 'vote:'):
            self._member.append(self._tag + data.strip())
            self._tag = ''

url = "http://www.qiushibaike.com/hot/page/"
page = 1
try:
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = { 'User-Agent' : user_agent }
    req = ur.Request(url + str(page), headers = headers)
    response = ur.urlopen(req)
    data = response.read().decode('utf-8')
    parser = qiubaiParser()
    parser.feed(data)
    for i in parser._all:
        print(i)

except ue.URLError as e:
    if hasattr(e, "code"):
        print(e.code)
    if hasattr(e, "reason"):
        print(e.reason)