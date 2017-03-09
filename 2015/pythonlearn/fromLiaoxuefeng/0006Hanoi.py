#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Move n Hanois from a to c with b
indent = 0
def hanoi(n):					# n: positive integer  
    global indent
    indent = n
    hanoiInter(n, 'a', 'b', 'c')
	
def hanoiInter(n, a, b, c):   
    indentIn = n	
    if n == 1:
        hanoiMove(a, c, indentIn)
    else:
        hanoiInter(n - 1, a, c, b)
        #HanoiInter(1, a, b, c)
        hanoiMove(a, c, indentIn)
        hanoiInter(n - 1, b, a, c)

showLen = len("%s --> %s")		# print(len("%s --> %s"))
indentMultiple = 1		
def hanoiMove(a, b, indentIn):
    #global indent
    print(indentIn, "%s --> %s".rjust(showLen + indentMultiple * (indent - indentIn)) %(a, b))
		
#Test#
hanoi(4)
