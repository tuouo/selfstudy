#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from datetime import datetime, date, time
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
        elif ('class', 'clear') in attrs:
            self._info.append(self._mess)
            self._mess = []

    def handle_data(self, data):
        if self._tag == "lastResponse":
            self._tag = ""
            data = data.strip()
            if data != "":
                if ":" in data:
                    times = time(int(data.split(":")[0]), int(data.split(":")[1]))
                    self._mess.append(datetime.combine(date.today(), times).__str__())
                elif "-" in data:
                    self._mess.append(data)


def getAllPages(path, url, pageBegin, pageEnd):
    dirs = 1 if pageEnd > pageBegin else -1
    for page in range(pageBegin, pageEnd, dirs):
        try:
            pageChange = str((page) * 50)
            req = ur.Request(url + pageChange)
            response = ur.urlopen(req)
            data = response.read().decode('utf-8', 'ignore')
            parser = allPageParser()
            parser.feed(data)
            print("get page %s ok." % (page + 1))
            with open(path, "a") as info:
                # print(type(info))
                for i in parser._info[::dirs]:
                    info.write(str(i) + "\n")     
        except ue.URLError as e:
            if hasattr(e, "code"):
                print(e.code)
            if hasattr(e, "reason"):
                print(e.reason)
    print("write ok.")

if __name__ == '__main__':
    url = "http://tieba.baidu.com/f?kw=%E4%BC%AA%E9%98%BF%E9%B2%81%E7%BA%B3%E6%81%B0%E5%B0%94%E9%82%A6&ie=utf-8&tp=0&pn="
    # path = os.path.join(os.getcwd(), "resource", "zangnan", "posts.rtf")
    # pageBegin = 129 - 1
    # pageEnd = 0
    # getAllPages(path, url, pageBegin, pageEnd)
    path = os.path.join(os.getcwd(), "resource", "zangnan", "new.rtf")
    pageBegin = 0
    pageEnd = 2
    getAllPages(path, url, pageBegin, pageEnd)