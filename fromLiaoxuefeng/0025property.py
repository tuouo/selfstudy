#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class Student(object):
    @property
    def score(self):
        return self._score
	
    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError("Integer needed")
        if value < 0 or value > 100:
            raise ValueError("score is between 0 and 100")
        self._score = value

s = Student()
s.score = 60
print(s.score)

class People(object):
    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age2015(self):
        return 2015 - self._birth

p = People()
p.birth = 1990
print(p.birth)
print(p.age2015)
