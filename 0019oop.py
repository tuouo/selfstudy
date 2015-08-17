#!/usr/bin/env python
# -*- coding: utf-8 -*-
std1 = { 'name': 'lily', 'score': 98 }
std2 = { 'name': 'Bob', 'score': 81 }

def printScore(std):
    print('%s: %s' % (std['name'], std['score']))
printScore(std1)
printScore(std2)


class Student(object):						# object may omit
    def __init__(self, name, score):		# self point to instance
        self.name = name
        self.score = score
		
    def printScore(self):
        print('%s: %s' % (self.name, self.score))
		
    def getGrade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 70:
            return 'B'
        else:
            return 'C'
	
    def doNothing(self, nothing):			# need *nothing(argument)
        print('doNothing' + nothing)
		
tuouo = Student('tuouo', 67)
miaoiao = Student('miaoiao', 83)
print(tuouo, miaoiao)
tuouo.age = 23								# ****
print(tuouo.name, tuouo.score, tuouo.age, tuouo.getGrade())

miaoiao.score = 91
tuouo.printScore()
miaoiao.printScore()
print(Student)
print(tuouo.getGrade)
print(Student.getGrade)
print(tuouo.doNothing(" haha"))