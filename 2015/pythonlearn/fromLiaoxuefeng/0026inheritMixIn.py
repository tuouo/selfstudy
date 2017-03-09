#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class Animal(object):
    def eat():
        print("Aniaml eating....")
		
class Runnable(Animal):
    pass
#    def eat():
#        print("Runnable eating...")	
		
class Flyable(Animal):
    def eat():
        print("Flyable eating...")
		
class Bat(Runnable, Flyable):
    pass
	
# 1st, search Runnable; 2nd, search Flyable; 3rd, Animal
Bat.eat()
print(issubclass(Bat, Animal))