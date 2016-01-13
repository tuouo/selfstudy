#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from html.parser import HTMLParser
import urllib.request as ur, urllib.error as ue, os, re

class urlPostParser(HTMLParser):
    def __init__(self):
        super(urlPostParser, self).__init__()
        self._tag, self._info = "", ""
        self._mess, self._all = [], []

    def handle_starttag(self, tag, attrs):
        if tag == "img" and self._tag == "data:":
            pass
        elif (('class', 'l_post j_l_post l_post_bright  ') in attrs or
            ('class', 'l_post j_l_post l_post_bright noborder ') in attrs):
            for i in attrs:
                if i[0] == "data-field":
                    self._mess.append(getFloorStr(getFloorInfo(i[1].replace('"', ""))))
        elif ('class', 'd_post_content j_d_post_content  clearfix') in attrs:
            self._tag = "data:"      

    def handle_data(self, data):
        if self._tag == "data:":
            data = data.strip() + '\n'
            self._info += data            

    def handle_endtag(self, tag):
        if tag == "div" and self._tag == "data:":
            self._mess.append(self._info)
            self._all.append(self._mess)
            self._tag, self._info = "", ""
            self._mess = []

def getFloorInfo(allInfo):
    one   = {}
    name  = re.findall("name_u:(\S.+)&", allInfo)[0].replace("%", r"\x")
    one["name_u"]      = name.encode('latin1').decode('unicode_escape').encode('latin1').decode('utf-8')
    one["post_no"]     = re.findall("post_no:(\d+),", allInfo)[0]
    one["date"]        = re.findall("date:(.{16}),", allInfo)[0]
    one["post_id"]     = re.findall("post_id:(\d+),", allInfo)[0]
    one["comment_num"] = re.findall("comment_num:(\d+),", allInfo)[0]
    return one

def getFloorStr(one):
    return "%s, %s, %s, %s, %s" % (one["post_no"], one["name_u"], one["date"], one["post_id"], one["comment_num"]) 

def getOnePost(url, path):           
    response = ur.urlopen(url)
    data = response.read().decode('utf-8', 'ignore')
    parser = urlPostParser()
    parser.feed(data)
    with open(newFile, "wb") as testfile:
        for i in parser._all:
            for j in i:
                testfile.write(j.encode('utf-8') + b"\r\n")

if __name__ == '__main__':
    url = "http://tieba.baidu.com/p/4147438587"
    path = os.path.join(os.getcwd(), "resource", "zangnan")
    newFile = os.path.join(path, "test1.rtf")
    getOnePost(url, path)
    print("OK, %s" % url)

# path = os.path.join(os.getcwd(), "resource", "zangnan")
# url = "http://tieba.baidu.com/"
# newFile = os.path.join(path, "new.rtf")
# with open(newFile, "rb") as urls:
#     for i in urls:
#         num = i.split(b"'")[1].decode('utf-8')
        # print(num)
        # url = "http://tieba.baidu.com/p/4147438587"
        # req = ur.Request(url)
        # # req = ur.Request(url + num)
        # response = ur.urlopen(req)
        # data = response.read().decode('utf-8', 'ignore')
        # parser = urlPostParser()
        # parser.feed(data)
        # for i in parser._all:
        #     print(i)
        
