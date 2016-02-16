#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" difference between 'is' and '=='
The statement 'is' is used for object identity, it checks if objects refer to the same instance
(same address in memory). (ob1 is ob2) means (id(ob1) == id(ob2))
And the '==' statement refers to equality (same value).

as a rule, a is b implies a == b 
(except for odd things like floating point NaNs that compare inequal to themselves)
"""

class foo(object):
    def __eq__(self, other):
        """ '=='is ultimately determined by the __eq__() method """
        return True

if __name__ == '__main__':
    f = foo()
    print(f)
    print(f == None)  # True
    print(f is None)  # False
    
    list1 = [1, 2, 3]
    list2 = [1, 2, 3]
    print(id(list1), id(list2))
    print(list1 == list2)
    print(list1 is list2)
    
    print(None is None)  # None is a singleton operator
    print(None == None)
    print(id(None))