#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pickle
d = dict(name = "Bob", age = 20, score = 88)
print(pickle.dumps(d))		# pickling subject to bytes

with open('test.txt', 'wb') as f:
    pickle.dump(d, f)		#pickling amd write to file-like Object

with open('test.txt', 'rb') as f:
    dd = pickle.load(f)		# direct from file-like Object to subject
    print(dd)				# dd is not d, only have same value
# but it is need python, version, strictly
# JSON will handle this problem

import json
print(json.dumps(d))		# Standard JSON str, "", above is ''. 

json_str = '{"age": 20, "score": 88, "name": "Bob"}'		# right
#json_str = "{'age': 20, 'score': 88, 'name': 'Bob'}"		# wrong, name should in double quotes
print(json.loads(json_str))


class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score
s = Student('Bob', 20, 88)
#print(json.dumps(s))		# TypeError: not JSON serializable
# because dumps don't know how to create JSON object, need tell it by default parameter

def student2Dict(std):
    return {'name': std.name, 'age': std.age, 'score': std.score}
	
print(json.dumps(s, default = student2Dict))
# for universal 
print(json.dumps(s, default = lambda obj: obj.__dict__))
# instance of class has attribute __dict__, store instance variable

# However , student2Dict --> Student
def dict2Student(d):
    return Student(d['name'], d['age'], d['score'])
print(json.loads(json_str, object_hook = dict2Student))
