#!/usr/bin/env python3
# -*- coding: utf-8 -*-
path = 'C:/Users/tuouo_000/gits/PythonLearn/'		# path: change \ to /

try:
    f = open(path + '0000Hello.py', 'r')	
    print(f.read())
finally:
    if f:
        f.close()
		
# do same function, and for short
with open(path + '0000Hello.py', 'r') as f:
    print(f.read())
	
with open(path + '0000Hello.py', 'r') as f:
    for line in f.readlines():
        print(line, end = '')
		
with open(path + '12321.jpg', 'rb') as f:			# read binary
    #print(f.read())
	pass
	
# if read a file which not UTF-8 encoding, open need 'encdoing' parameter
# open("XXXpathXXX", 'r', encoding = 'gbk')		# read 'gbk' file for example

# if some unknown coding lead to UnicodeDecodeError, parameter can manage it
# open("XXXpathXXX", 'r', encoding = 'gbk', errors = 'ignore') #ignore for example


wf = open(path + 'test.txt', 'w')			# means write file
wf.write("Hello world")						# write to cache, later to file
wf.close()									# in this time, things will sure to file
# recommand
with open(path + 'test.txt', 'w') as wf:
    wf.write('Hello world2')				# will cover pre write
# also, encoding is works. we can write file in designate encoding