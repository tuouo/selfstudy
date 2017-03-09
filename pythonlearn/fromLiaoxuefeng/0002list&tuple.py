#!/usr/bin/env python3
# -*- coding: utf-8 -*-
students = []
print(len(students))
students = ["tuouo", "miaoiao", "oo", "xx"]
print(students, len(students))
print(students.sort())
students.append(["haha", "xixi", "Lily"])
#students.sort()		error
print(students, len(students))
students.insert(5, 5566)
print(students, len(students))
students.pop()
print(students, len(students))
students.pop(2)
print(students, len(students))
for name in students:
    print(name)
print()

number = ()
print(number, len(number))
number = (1)
print(number)			#print(number, len(number)) error
number = (1,)			#number = ( , 1)	error
print(number, len(number))
number = (1, ['2', "201", '202'],"345")
print(number, len(number))
number[1][2] = 2
print(number, len(number))

if 23:
    print(number[-2][-1])
if []:
    print(number[1][-2])
elif 'a':
    print(number[1])

sum = 0
for n in list(range(100)):
    sum += n
print(sum)
n = 99
while n > 0:
    sum -= n
    n -= 1 				#Ctrl + c : if endless loop
print(sum)
