#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging
logging.basicConfig(
    level    = logging.INFO,
    format   = '|%(asctime)s|%(filename)s[line:%(lineno)s] %(levelname)s\n%(message)s',
    datefmt  = '%a, %d %b %Y %H:%M:%S',
    filename = 'test.log',
    filemode = 'w'
	)

##########################################################
# This is contribute to console only
console = logging.StreamHandler()
console.setLevel(logging.WARNING)
formatter = logging.Formatter('%(name)-12s: %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)
##########################################################

logging.info("This is logging test of INFO")
logging.debug("This is logging test of debug")
logging.warning("This is logging test of warning")