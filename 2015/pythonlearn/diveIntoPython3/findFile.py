#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import glob, os
files = [f for f in glob.glob('*test*.py')] 	#  Lib/glob.py
print(glob.glob(r'c:\*.otf'))
print(glob.glob(r'E:\pic\*\*.jpg'))
print(glob.glob(r'../*.py'))


def findFile(pattern = 'txt', root = '.'):
    files = []
    for x in os.listdir(root):
        path = os.path.join(root, x)	
        if os.path.isfile(path) and pattern in x:	# os.path.isfile(path), path not x
            files.append(path)
        elif os.path.isdir(path):	
            files += findFile(pattern, path)    	
    return files

def findFile2(pattern = 'txt', root = '.'):
    dirs, files = [], []
    for x in os.listdir(root):
        path = os.path.join(root, x)	
        if os.path.isfile(path) and pattern in x:	# os.path.isfile(path), path not x
            files.append(path)	
        elif os.path.isdir(path):	
            dirs.append(path)
    for dir in dirs:
        files += findFile(pattern, dir)	            

print(findFile('exe', 'C:\\Python34'))
#findFile('.txt')
#findFile('Except')
#findFile('exe', 'C:\\soft')
#findFile('user', 'C:\\Users\\tuouo_000\\Documents\\Python\\Code')   