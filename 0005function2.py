#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def calc(numbers):
    sum = 0
    for n in numbers:
        sum += n * n
    return sum
print('calc([]):', calc([]))
print('calc([1, 2, 3]):', calc([1, 2, 3]))

def calc2(*numbers):
    sum = 0
    for n in numbers:
        sum += n * n
    return sum
print('calc2():', calc2())
print('calc2(1, 2, 3):', calc2(1, 2, 3))
nums = [1, 2, 3]
print('calc2(1, 2, 3):', calc2(*nums))

def joinStr(*args):
    if (len(args) == 0): 
        pass
    else: 
        print('%s!' % ('+'.join(args))) 
joinStr('1', '2', '3')
def joinNum(*args):
    if (len(args) == 0): 
        pass
    else:         
        #print('%s!' % ('+'.join(str(args)))) 
        print('%s!' % ('+'.join(str(args)))) 
joinNum(1, 2, 3)
print(str(nums), len(str(nums)))
for i in str(nums):
    print("=" + i + "=", end ='')
print()
############################################
def person(name, age, **kw):
    print("name:%s, age:%s, other:%s"%(name, age, kw))
    #print('name:', name, 'age:', age, 'other:', kw)
    for n in kw:
        kw[n] = ''
person('Lily', 19)
#person('Dick', 21, 'Hangzhou', 'Teacher')	error, postional arguments only 2
person('Dick', 21, city = 'Hangzhou', job = 'Teacher')
extra = {'city': 'Hangzhou', 'job': 'Teacher'}
person("Mack", 14, **extra)
print("extra:", extra)
for n in extra:    
    extra[n] = ''
print("extra:", extra)
############################################
def person(name, age, *, city = 'Hangzhou', job):
    print(name, age, city, job)
person("Lily", 24, city = "shaoxin", job = 'Teacher')
person("Lily", 24, job = 'Teacher')


def f1(a, b, c = 0, *args, **kw):
	print("a:%s, b:%s, c:%s, args:%s, kw:%s" %(a, b, c, args, kw))
    #print("a:", a, ",b:", b, ',c:', c, ',args:', args, ',kw:', kw)
def f2(a, b, c = 0, *, d, **kw):
    print("a:%s, b:%s, c:%s, d:%s, kw:%s" %(a, b, c, d, kw))
f1(1, 0)
f1(1, 2, 3)
f1(1, 2, 3, 4, 5)
f1(1, 2, 3, 4, 5, 6, x = 7)
f2(1, 2, d = 99, ext = None)

args = (1, 2, 3, 4)
kw = {'d':99, 'x':'#'}
f1(*args, **kw)
args = (1, 2, 3)
f2(*args, **kw)