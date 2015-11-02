#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# TDD: Test-Driven Development
class Dict(dict):
    def __init__(self, **kw):
        super().__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError("'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value
		
d = Dict(a = 1, b = 2)
print(d['a'], d.a, d.b)
d.b = 3
print(d.b, '\n')

import unittest
class TestDict(unittest.TestCase):
    def test_init(self):				# test method need start with test_(test_XXX)
        d = Dict(a = 1, b = 'test')
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')

    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')
		
    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']
	
    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty
        		
    def setUp(self):							# run before every test
        print('setUp...............')

    def tearDown(self):							# run after every test
        print('tearDown..')	
    # By combine setUp & tearDown, we need do same things in every 
	
if __name__ == '__main__':
    unittest.main()

# python3 0033uniteTest.py
# python3 -m unittest 0033uniteTest  #recommend(batch process)