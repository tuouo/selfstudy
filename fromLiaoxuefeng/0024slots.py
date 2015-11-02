#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class Student(object):
    __slots__ = ('name', 'age', 'setAge')	# setAge is needed
	
sTuouo = Student()
sTuouo.name = 'tuouo'
print(sTuouo.name)

def setAge(self,age):
    self.age = age

from types import MethodType
sTuouo.setAge = MethodType(setAge, sTuouo)	# ....
sTuouo.setAge(25)
print(sTuouo.age)
del sTuouo.age				# can delete

s2 = Student()
s2.age = 20
print(s2.age)
Student.setAge = MethodType(setAge, Student)
s2 = Student()
s2.setAge(38)
print(s2.age)
#s2.score = 100				# no attribute, no in __slots__
sTuouo.setAge(24)
print(s2.age, sTuouo.age, Student.age)	# same!!!
#del sTuouo.age				# can't, Student attribute, read-only
#s2.age = 20				# can't, Student attribute, read-only

class StudentGraduated(Student):
    pass
g = StudentGraduated()
g.age = 100					# father __slots__ doesn't matter
print(g.age)