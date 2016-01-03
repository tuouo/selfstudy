#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os, mmap
path = os.path.join(os.getcwd(), "resource", "zangnan", "test.rtf")
# with open(path, "wb") as f:
#     f.write(b"Hello Python!\nPython Hello!\n")

# with open(path, "r+b") as f:
#     mm = mmap.mmap(f.fileno(), 0)
#     print(mm.readline())
#     print(mm[:5])
#     mm[6:] = b" world!\n"    # mmap slice assignment is wrong size
#     mm.seek(0)
#     print(mm.readline())
#     mm.close()


mm = mmap.mmap(-1, 14)
mm.write(b"Hello world!")
pid = os.getpid()
print(pid)
# if pid == 0:
#     mm.seek(0)
#     print(mm.readline())
#     mm.close()
mm.seek(0)
print(mm.readline())
mm.close()