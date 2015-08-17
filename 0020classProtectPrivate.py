#!/usr/bin/env python3
# -*-coding: utf-8 -*-
class Student(object):						
    def __init__(self, name, score):		
        self.__name = name			# define private variable
        self.__score = score		# __XXX not __XXX__(this can visit)
									# if _XXX, it can be visit but hope not
    def getName(self):
        return self.__name
	
    def getScore(self):
        return self.__score
		
    def printScore(self):
        print('%s: %s' % (self.__name, self.__score))
		
    def setScore(self, score):
        if 0 <= score <= 100:		# needn't XXX and XXX
            self.__score = score
        else:
            raise ValueError('bad score')
		
    def getGrade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 70:
            return 'B'
        else:
            return 'C'
			
tuouo = Student('tuouo', 67)
#print(tuouo.name, tuouo.score, tuouo.age)			# has no attribute
print(tuouo._Student__name, tuouo._Student__score)	# however, however
tuouo.setScore(78)				# -8, raise
print(tuouo.getScore())

print(hasattr(tuouo, 'score'))						
tuouo.age = 23
print(hasattr(tuouo, 'age'))						# need ' '
print(setattr(tuouo, 'name', 'zaizi'))
print(getattr(tuouo, 'name'))
print(getattr(tuouo, 'ss', 404))					#set return 404, if not exist