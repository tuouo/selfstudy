#!/usr/bin/env python3
# -*- coding: utf-8 -*-
a = 2 # '10', 10, 0
try:
    print("In try...")
    r = 10 / a	
    print('reslut: ', r)
except TypeError as e:
    print('TypeError: ', e)
except ZeroDivisionError as e:
    print('except: ', e)
else:
    print('No error')
finally:						# option
    print('Finally...')
print('End\n')


def testDivis(s):
    return 10 / int(s)

def selfDouble(s):
    return 2 * testDivis(s)

import logging
def main(s):
    try:
        selfDouble(s)
    except Exception as e:		# except needn't follow code
        print('Error:', e)
        #logging.exception(e)	# can backup to log File, in some way
    finally:
        print('finally...')
		
main('0')
print('.....')


class someError(ValueError):	# only necessary, then define it
    pass
	
def someTest(s):
    if s == 0:
        raise someError('invalid value: %s' % s)	
    return 10 / s
someTest(1)						# if raise, program stop
print(',,,,,,')

def someOther():
    try:
	    someTest(0)
    except ValueError as e:
        print('something')
        #raise					# just raise pre except
        raise ZeroDivisionError()
someOther()