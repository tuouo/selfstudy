#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import urllib.request as ur, urllib.error as ue, re, os
from html.parser import HTMLParser
from datetime import datetime, date, time
from getItemData import getDateTime, getLastData, path, url

class allPageParser(HTMLParser):
    def __init__(self, day = None):
        super(allPageParser, self).__init__()
        self._info = []
        self._mess = []
        self._tag = ""
        self._day = day
        self._goOn = True

    def handle_starttag(self, tag, attrs):
        if self._goOn:    	
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
    	if self._goOn:
            if self._tag == "lastResponse":
                self._tag = ""
                data = data.strip()
                if data != "":
                    print(data)   
                    if ":" in data:
                        times = time(int(data.split(":")[0]), int(data.split(":")[1]))
                        day = datetime.combine(date.today(), times)
                        if self._day and day < self._day:
                            self._goOn = False
                        if self._goOn:
                            self._mess.append(day.__str__())
                    elif "-" in data:
                        self._mess.append(data)

def getAllPages(path, url, pageBegin, pageEnd, day):
    dirs = 1 if pageEnd > pageBegin else -1
    for page in range(pageBegin, pageEnd, dirs):
        try:
            pageChange = str((page) * 50)
            req = ur.Request(url + pageChange)
            response = ur.urlopen(req)
            data = response.read().decode('utf-8', 'ignore')
            parser = allPageParser(day)
            parser.feed(data)
            count += len(parser._info)
            with open(path, "a+b") as info:
                for i in parser._info[::dirs]:
                    info.write(str(i).encode('utf-8') + b"\r\n") 
            print("get page %s ok.  All: %s" % (page + 1, count))
            if not parser._goOn:
                break
        except ue.URLError as e:
            if hasattr(e, "code"):
                print(e.code)
            if hasattr(e, "reason"):
                print(e.reason)
    print("write ok.")



if __name__ == '__main__':
    # path = os.path.join(path, "posts.rtf")
    # pageBegin, pageEnd = 129 - 1, 0
    # getAllPages(path, url, pageBegin, pageEnd, None)
    pathNew = os.path.join(path, "new.rtf")
    pageBegin, pageEnd = 0, 10
    day = getDateTime(getLastData("posts.rtf"))
    print(day)
    getAllPages(path, url, pageBegin, pageEnd, day)