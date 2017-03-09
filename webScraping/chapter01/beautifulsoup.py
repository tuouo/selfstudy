#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        print(e)
        return None
    try:
        bsObj = BeautifulSoup(html.read(), "html.parser")
        title = bsObj.body.h1
    except AttributeError as e:
        return None
    return title

if __name__ == '__main__':
    title = getTitle("http://pythonscraping.com/pages/page1.html")
    if title == None:
        print("Title could not be found")
    else:
        print("Title:{}".format(title))