#!/usr/bin/env python3
# -*- coding: utf-8 -*-
suffixes = {1000 : ['KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'],
            1024 : ['KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB']}

def approximate_size(size, kilobyte_is_1024_bytes = True):
    '''Convert a file size to short.

    Keyword agruments:
    size -- file size in bytes
    kilobyte_is_1024_bytes -- if True(default), use multiples of 1024
                              if False, use multiples of 1000

    return string

    '''
    if size < 0:
        raise ValueError('number must be nonnegative')

    multiple = 1024 if kilobyte_is_1024_bytes else 1000
    for suffix in suffixes[multiple]:
        size /= multiple
        if size < multiple:
            return '{0:.2f} {1}'.format(size, suffix)
    else :
        raise ValueError('number too large')

import unittest
class tApproximate(unittest.TestCase):
    def test_approximate(self):
        self.assertEqual(approximate_size(1000000000000, False), '1.00 TB')
        self.assertEqual(approximate_size(1000000000000), '931.32 GiB')        

if __name__ == '__main__':
    unittest.main()