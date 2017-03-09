#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from html.parser import HTMLParser
from html.entities import name2codepoint

# !!! warning!!! 
# DO NOT SAVE HTML PAGE UTILIZE IE OR SPARTA OR ANYTHING ELSE OF MICROSOFT
# !!! warning!!!

class exampleHTMLParser(HTMLParser):
    def __init__(self):
        super(exampleHTMLParser, self).__init__()
        self._tag = ''
		
    def handle_starttag(self, tag, attrs):
        if ('class', 'event-title') in attrs:
            self._tag = 'Title:'
        elif ('class', 'event-location') in attrs:
            self._tag = 'Location:'
        elif tag == 'time':
            self._tag = 0		
			
    def handle_data(self, data):
        if self._tag in ('Title:', 'Location:'):
            if self._tag == 'Title:':
                print('-' * 30)
            print(self._tag, data.strip())	# some message from HTML turn garbled
            self._tag = ''			
        if isinstance(self._tag, int):
            if self._tag > 2:
                self.tag = ''
            else:
                links = [' -- ', '\t', '\n']
                print(data.strip(), end = links[self._tag])
                self._tag += 1
			
parser = exampleHTMLParser()
path = 'C:/Users/tuouo_000/gits/PythonLearn/resource/'
with open (path + 'Our Events _ Python.org.html', 'r') as html:
    parser.feed(html.read())				#.decode('gbk').encode('utf-8')