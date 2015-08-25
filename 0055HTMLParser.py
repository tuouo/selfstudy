#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from html.parser import HTMLParser
from html.entities import name2codepoint

class selfHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print('1<%s>' % tag, end = '')

    def handle_endtag(self, tag):
        print('2</%s>' % tag, end = '')
		
    def handle_startendtag(self, tag, attrs):
        print('3<%s/>' % tag, end = '')

    def handle_data(self, data):
        print(data, end = '')

    def handle_comment(self, data):				# distinguish by '<!'
        print('4<!--', data, '-->', end = '')

    def handle_entityref(self, name):
        print('5&%s;' % name, end = '')
		
    def handle_charref(self, name):
        print('6&#%s;' % name, end = '')	
		
parser = selfHTMLParser()
parser.feed('''<html>
<head></head>
<body>
<!-- test html parser --><!
    <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
</body></html>''')		