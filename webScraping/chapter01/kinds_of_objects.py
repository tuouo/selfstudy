#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup


soup = BeautifulSoup('<b class="boldest">Extremely bold</b>', 'html.parser')
tag = soup.b
print(tag, type(tag))

print(tag.name)
tag.name = "blockquote"
print(tag.name, tag)

print(tag['class'])		# tag.class : error
print(tag.attrs)
tag['class'] = "verybold"
tag['id'] = 1
print(tag)
del tag['class']
del tag['nothing']		# doesn't matter
del tag['id']
print(tag)
#print(tag['class'])	# keyError
print(tag.get('class'))

print(tag.string, type(tag.string))
# unicode_string = unicode(tag.string)
# print(unicode_string, type(unicode_string))
tag.string.replace_with("No longer lold")
print(tag)

id_soup = BeautifulSoup('<p id="my id"></p>', 'html.parser')
print(id_soup.p['id'])	# not a multi-valued attribute
rel_soup = BeautifulSoup('<p>Back to the <a rel="index">homepage</a></p>', 'html.parser')
print(rel_soup.a['rel'])
rel_soup.a['rel'] = ['index', 'contents']
print(rel_soup.p)
print(rel_soup.a['rel'])


markup = "<b><!--Hey, buddy. Want to buy a used parser?--></b>"
soup = BeautifulSoup(markup, "html.parser")
comment = soup.b.string
print(type(comment), comment)
print(soup.b.prettify())

from bs4 import CData
cdata = CData("*A cdata block*")
comment.replace_with(cdata)
print(soup.b.prettify())