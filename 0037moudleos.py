#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
import os
# posix: Linux, Unix, Mas OS X; nt: Windows
print(os.name)
#print(os.uname())		# unsupport on windows, --> AttributeError

#print(os.environ)		# show environment variable message
print(os.environ.get('PATH'))
print(os.environ.get('X', 'default'))

abspath = os.path.abspath('.')
print(abspath)
abspath = os.path.join(abspath, 'testdir')
# method join will join path suit current os
print(abspath)
print(os.mkdir(abspath))	# None, if file already exist, --> FileExistsError
print(os.rmdir(abspath))	# None

# abspath needn't really exist, methods which under treat abspathas str
print(os.path.split(abspath))
# slip path. \aaa\bbb\ccc\ddd --> (\aaa\bbb\ccc, ddd)
print(abspath)	# abspath value not change
abspath = os.path.split(abspath)[0]
print(abspath)
abspath = os.path.join(abspath, 'test.txt')
print(abspath)
print(os.path.splitext(abspath))
# slip path. \aaa\bbb\ccc\ddd.??? --> (\aaa\bbb\ccc\ddd, .???)
print(abspath)

abspath = os.path.abspath('.')
print(abspath)
os.rename('test.txt', 'texttest.txt')
os.rename('texttest.txt', 'test.txt')

#print([x for x in os.listdir('.')])	# show all File in current path 
print([x for x in os.listdir('.') if os.path.isdir(x)])
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.txt'])


def findFile(pattern = 'txt', root = '.'):
    for x in os.listdir(root):
        path = os.path.join(root, x)	
        if os.path.isfile(path) and pattern in x:	# os.path.isfile(path), path not x
            print(path)		
        elif os.path.isdir(path):	
            findFile(pattern, path)		
			
findFile()
#findFile('.txt')
#findFile('Except')
#findFile('exe', 'C:\\soft')
#findFile('user', 'C:\\Users\\tuouo_000\\Documents\\Python\\Code')

def findFile2(pattern = 'txt', root = '.'):
    dirs = []
    for x in os.listdir(root):
        path = os.path.join(root, x)	
        if os.path.isfile(path) and pattern in x:	# os.path.isfile(path), path not x
            print(path)		
        elif os.path.isdir(path):	
            dirs.append(path)
    for dir in dirs:
        findFile(pattern, dir)	