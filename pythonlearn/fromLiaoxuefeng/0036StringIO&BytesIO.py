#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
from io import StringIO
f = StringIO()
print(f.write('hello'))		# return write data's length
print(f.write(' '))
print(f.write('world!'))
print(f.readline())			# print nothing. f.write() and f.readline() cann't work in same time
print(f.getvalue())

f = StringIO('Hello!\nHi!\nGoodBye!')
ff = f
print(ff.readlines())		# if 'ff' read means 'f' also read, so nothing left in 'f'
while True:
    s = f.readline()		
    if s == '':
        break
    print(s, end = '')
	
from io import BytesIO
f = BytesIO()
print(f.write('中文'.encode('utf-8')))			# len: 6
print(f.getvalue())

f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')		# need write utf-8 endcoding bytes
print(f.read())