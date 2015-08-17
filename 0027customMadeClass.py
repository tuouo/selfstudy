#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class Student(object):
    def __init__(self, name = 'tuouo'):
        self.name = name			
#print(Student('tuouo'))		# <__main__.Student object at ...
		
    def __str__(self):
        return 'Student object (name: %s)' %self.name
#print(Student('tuouo'))		# Student object (name: ...

    __repr__ = __str__			# same implement, by short in this way
# >>>Student('tuouo')
	
    def __call__(self, name):
        self.name = name
        print("My name is %s" % self.name)
Student()("Haha")				# __call__
print(Student('tuouo'))


class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1
	
    def __iter__(self):			# need return iteration
        return self
		
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b	
        if self.a > 100:
            raise StopIteration();
        return self.a
for i in Fib():					# after above prepare, can run in this way
    print (i, ' ', end = '')		
print()
#Fib()[5]						# this still cann't

class Fib2(object):
    def __getitem__(self, n):
        a , b = 0, 1
        for x in range(n):
            a, b = b, a + b
        return a
for i in range(1, 10):
    print(Fib2()[i], ' ', end = '')
print()
	
# so how about XXX[a:b]
class Fib3(object):
    def __getitem__(self, n):
        #if isinstance(n, int):	# see Fib2
        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for i in range(stop):
                if i >= start:
                    L.append(a)
                a, b = b, a + b
            return L
print(Fib3()[:5])			
print(Fib3()[4:7])	
# not do list below yet		
#print(Fib3()[4:7:2])	
#print(Fib3()[4:7:-1])	
			
class Student(object):
    def __init__(self):
        self.name = 'Tuouo'
# only has attr name, no others

    def __getattr__(self, attr):
        if(attr == 'score'):
            return 91
        raise AttributeError("'Student' object has no attribute '%s'" %attr)
print(Student().score)

# in __getattr__
# if(attr == 'age'):
#     return lambda: 25
# Student().age()
# only if no attr there, can __getattr__ been ran


class Chain(object):
    def __init__(self, path = '*'):
        self._path = path
    def __getattr__(self, path):
        if path == 'user':
            return Chain('%s/%s' %(self._path, 'tuouo'))    		
        #print(self._path, path)
        return Chain('%s/%s' %(self._path, path))        
    def __str__(self):
        return self._path
    __repr__ = __str__
print(Chain().user.status.timeline.list)
print(Chain('lala'))

