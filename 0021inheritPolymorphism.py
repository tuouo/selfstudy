#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class Animal(object):
    def run(self):
        print('Animal is running...')

class Dog(Animal):
    def run(self):
        print('Dog is running...')
		
class Cat(Animal):
    def eat(self):
        print('Where is mouse...')
		
dog = Dog()
dog.run()
cat = Cat()
cat.run()	
a = Animal()
print(isinstance(dog, Dog), isinstance(cat, Animal), isinstance(a, Dog))
print(type(dog), type(a))
print(dir(Dog))
print(dir(dog))
print(dir(cat))

def runAndRun(a):			# animal interchange is same
    a.run()
    a.run()

runAndRun(Dog())
runAndRun(dog)						# same as Dog()
runAndRun(Animal())

class sheep(object):
    def run(self):
        print('mie, mie, mie...')	
runAndRun(sheep())		