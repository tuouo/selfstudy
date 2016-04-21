#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import source


if __name__ == '__main__':
    soup = BeautifulSoup(source.html_doc, "html.parser")
    print(soup.prettify())
    print(soup.title)
    print(soup.title.name)
    print(soup.title.string)
    print(soup.title.parent.name)
    print(soup.p)
    print(soup.p['class'])
    print(soup.a)
    print(soup.find_all('a'))    
    print(soup.find(id="link3"))
    for item in soup.find_all('a'):
        print(item.get('href'))
    print(soup.get_text())