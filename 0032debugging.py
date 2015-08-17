#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def testDebugging(s):
    n = int(s)
    print('...n = %d' %n)		# 1st, print
    assert n != 1, 'n is 1!'	# 2nd, assert. 
	#command with -o to close assert, but need in python command line
    return 10 / n	
	
testDebugging('2')

import logging
logging.basicConfig(level = logging.DEBUG)	#DEBUG, INFO, WARNING, ERROR
s = '0'
n = int(s)
logging.info('n = %d' %n)
print(10 / n)


# command "-m pdb" 
#     command "1" to see code status
#     command "1" to run by step
#     command "p XXX" to see XXX status
#     command "q" to quit

# pdb.set_trace()
# when in command "-m pdb" stage 
# will automate run to code pdb.set_trace() than stop
# after it,  command "p XXX" to see XXX status
#            command "c" to run continue


