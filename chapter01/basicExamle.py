#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from urllib.request import urlopen

if __name__ == "__main__":
    html = urlopen("http://pythonscraping.com/pages/page1.html")
    print(html.read())
    html2 = urlopen("http://www.pythonscraping.com/exercises/exercise1.html")
    print(html2.read())
    print(html2 == html)    
    print(html2.read() == html.read())