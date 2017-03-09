#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from html.parser import HTMLParser
import string, re
alphablet = string.ascii_lowercase

class urlPostParser(HTMLParser):
    def __init__(self):
        super(urlPostParser, self).__init__()
        self._tag, self._info, = "", ""
        self._count, self._Item = 0, {}
        self._img, self._mess, self._all = {}, [], []

    def handle_starttag(self, tag, attrs):
        if self._tag == "data:":
            if tag == "img":
                for i in attrs:
                    if i[0] == "src":
                        imgName = self._Item["post_no"] + alphablet[self._count] + ".png"
                        mgUrl, self._count = i[1], self._count + 1
                        self._img[imgName] = mgUrl
                        data = "IMAGE%s %s IMAGE" % (imgName, mgUrl)
                        self._info += data
            elif tag == "br":
                self._info += "\r\n"
        elif (('class', 'l_post j_l_post l_post_bright  ') in attrs or
            ('class', 'l_post j_l_post l_post_bright noborder ') in attrs):
            for i in attrs:
                if i[0] == "data-field":
                    self._Item = getReplyInfo(i[1].replace('"', ''))
                    self._mess.append(getReplyStr(self._Item))
        elif ('class', 'd_post_content j_d_post_content  clearfix') in attrs:
            self._tag = "data:"      

    def handle_data(self, data):
        if self._tag == "data:":
            data = data.strip()
            self._info += data            

    def handle_endtag(self, tag):
        if tag == "div" and self._tag == "data:":
            self._mess.append(self._info)
            self._all.append(self._mess)
            self._tag, self._info = "", ""
            self._count, self._mess = 0, []

def getReplyInfo(allInfo):
    one   = {}
    name  = re.findall("name_u:(\S+)&", allInfo)[0].replace("%", r"\x")
    one["name_u"]      = name.encode('latin1').decode('unicode_escape').encode('latin1').decode('utf-8')
    one["post_no"]     = re.findall("post_no:(\d+),", allInfo)[0]
    one["date"]        = re.findall("date:(.{16}),", allInfo)[0]
    one["post_id"]     = re.findall("post_id:(\d+),", allInfo)[0]
    one["comment_num"] = re.findall("comment_num:(\d+),", allInfo)[0]
    return one

def getReplyStr(one):
    return "%s, %s, %s, %s, %s" % (one["post_no"], one["name_u"], one["date"], one["post_id"], one["comment_num"])


class pageNumParser(HTMLParser):
    def __init__(self):
        super(pageNumParser, self).__init__()
        self._tag = False
        self._num = 1

    def handle_starttag(self, tag, attrs):
        if tag == "span" and [('class', 'red')] == attrs:
            self._tag = True

    def handle_data(self, data):
        if self._tag:
            self._num = int(data)
            self._tag = False