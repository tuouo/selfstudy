#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from hello import Hello
h = Hello()
h.Hi()
print(type(Hello), type(h))
# function type() create class Hello

def Bye(self, name = 'world'):
        print("Bye %s." %name)
Byebye = type("BB", (object,), dict(ByeBye = Bye))
# type('class name', father(tuple), method name & function)
b = Byebye()
b.ByeBye()
print(type(Byebye), type(b))	# class 'type', class '__main__.BB'
# same as import class


class ListMetaclass(type):		# necessary, original from type
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)
		
class MyList(list, metaclass = ListMetaclass):
    pass

l = MyList()
l.add("as'd")
print(l)

#L1 = list()
#L1.add('af')				# normal list has no attribute 'add'
