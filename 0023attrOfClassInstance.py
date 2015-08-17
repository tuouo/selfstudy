#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class Student(object):
    def __init__(self, name):
        self.name = name

sBob = Student('Bob')
sBob.score = 90
print(sBob.name)
s1 = Student
s2 = Student
print(s1 == s2)
sBob2 = Student('Bob')
print(sBob == sBob2)


class Student(object):		# this Student cover the one above
    name = 'Student'

s3 = Student
print(s1 == s3)				
#sLily = Student('Bob')		#object take no parameters
print(Student.name)
s = Student()
print(s.name)
s.name = 'tuouo'
print(s.name)				# instance attr cover class attr
del s.name
print(s.name)