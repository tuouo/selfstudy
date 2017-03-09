#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
print('\tProcess [%s] start ...' % os.getpid())
pid = 0#os.fork()		# 'module' has no attribute 'fork', can't works on windows
if pid == 0:
    print('\tChild process (%s), parent is (%s)' % (os.getpid(), os.getppid()))
else:
    print('\tprocess (%s) created a child process (%s).' % (os.getpid(), pid))

# above things will be run twice, cause underside code
	
from multiprocessing import Process
def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))

if __name__ == '__main__':
    print('Parent process %s.' %os.getpid())
    p = Process(target = run_proc, args = ('test',))
    print('Child process will start.')
    p.start()
    p.join()
    print('Child process end.')

# underside things will be run twice, cause same reason	
print('123', os.getpid())