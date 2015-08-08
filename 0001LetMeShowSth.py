#!/usr/bin/env python3
# -*- coding: utf-8 -*-
print('Hello World.', end = '')
print(" I'm tuouo.")
print("I\'m \"OK\".", '''I'm "OK".''', """Yeah, I'm really "OK".""")
#print(1,  , 2)						#error
#print(r'('''En, I'm "OK".''')')	#error
print(r'"I\'m \"OK\"."')
print(r'\t\\\t\\\0\\', '\t\\\t\\\0\\', '\t\\\t\\\0\\')
print('s3 = r\'Hello, "Dear"')
print("r'''Hello,")
print('''Lalalalalalal
lalala
....lalala							# ...
lala''')
print()
print('包含中文的str')
print(ord('a'), chr(66), ord('中'), chr(25991), chr(24333), '\u4e2d\u6587')
print('ABC', b'ABC')				#Unicode(bytes), ascii(pre byte)
print('ABC'.encode('ascii'), '中文'.encode('utf-8'))
print(b'ABC'.decode('ascii'), b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))
print(len('ABC'), len('中文'))
print(len(b'ABC'), len(b'\xe4\xb8\xad\xe6\x96\x87'), len('中文'.encode('utf-8')))

print("\n10 / 3 =", 10 / 3)
print("10 / 7 =", 10 / 7)			# 1 + 16
print("10 // 3 =", 10 // 3)
print('10 // 7 =', 10 // 7)
print('Hi, %s, you have $%d.'%('tuouo', 100000))
print('%.2f%%'%((85 - 72) * 100 / 72))	#print('%.2f'%85/72), 'str' and 'int'