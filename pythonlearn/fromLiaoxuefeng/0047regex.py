#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
print(re.match(r'^\d{3}\-\d{3,8}$', '010-12345'))		# ^ $
print(re.match(r'^\d{3}\s\d{3,8}$', '010	12345'))	#\s tab

def reMatch(regex, s):
    if re.match(regex, s):
        print('match')
    else:
        print('failed')

reMatch(r'[a-zA-Z\_][0-9a-zA-Z\_]*\d{6}\s+[B|ae]\w{2}', '__zip__310000	aD7')	# [B|ae]

# regex in split
s = 'a b   c '
print(s.split(' '))
print(re.split(r'\s+', s.strip()))
s = ' a, b ;  c '
print(re.split(r'[\s\,\;]+', s.strip()))

# more or less
rule1 = r'^(\d+)(0*)$'
rule2 = r'^(\d+?)(0*)$'
s = '102300'
print(re.match(rule1, s).groups())
print(re.match(rule2, s).groups())

# Group
rule = r'^(\d{3})-(\d{3,8})$'		# () group
s_phone = '020-12345'
m = re.match(rule, s_phone)
print(m.group(1), m.group(2), m.group(0))

# prepare
re_phone = re.compile(rule)
print(re_phone.match(s_phone).groups())


rule = r'^\w[\w\.]+@\w+.com$'
s = 'someone@outlook.com'
s1 = 'fag.ff@vr4.com'
reMatch(rule, s)
reMatch(rule, s1)
