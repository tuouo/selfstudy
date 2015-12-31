#!/usr/bin/env python3
# -*- cofing: utf-8 -*-
from html.parser import HTMLParser
import urllib.request as ur, urllib.error as ue, re, os
class allPageParser(HTMLParser):
    def __init__(self):
        super(allPageParser, self).__init__()
        self._info = []
        self._mess = []
        self._tag = ""

    def handle_starttag(self, tag, attrs):    	
        if ('class', 'j_th_tit') in attrs:
            for i in attrs:
                if i[0] in ("href", "title"):
                    self._mess.append(i[1])
        elif ('class', 'threadlist_reply_date j_reply_data') in attrs:
            self._tag = "lastResponse"

    def handle_data(self, data):
        if self._tag == "lastResponse":
            self._tag = ""
            self._mess.append(data.strip())
            self._info.append(self._mess)
            self._mess = []


if __name__ == '__main__':
    path = os.path.join(os.getcwd(), "resource", "zangnan", "posts.rtf")
    url = "http://tieba.baidu.com/f?kw=%E4%BC%AA%E9%98%BF%E9%B2%81%E7%BA%B3%E6%81%B0%E5%B0%94%E9%82%A6&ie=utf-8&tp=0&pn="
    pageEnd = 129 - 1
    pageBegin = 0

    for page in range(pageEnd, pageBegin, -1):
        try:
            pageChange = str((page) * 50)
            req = ur.Request(url + pageChange)
            response = ur.urlopen(req)
            data = response.read().decode('utf-8')
            parser = allPageParser()
            parser.feed(data)
            print("get page %s ok." % (page + 1))
            with open(path, "a") as info:
                # print(type(info))
                for i in parser._info[::-1]:
                    info.write(str(i) + "\n")     
        except ue.URLError as e:
            if hasattr(e, "code"):
                print(e.code)
            if hasattr(e, "reason"):
                print(e.reason)
    print("write ok.")