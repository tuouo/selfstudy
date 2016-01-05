#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os, mmap
path = os.path.join(os.getcwd(), "resource", "zangnan", "test.rtf")
with open (path, 'w') as f:
    # print("fileno:", f.fileno())
    for i in range(5):
        f.write("Hello, this is line %s.\n" % (i * str(i)))

with open(path, "r+b") as f:
    mm = mmap.mmap(f.fileno(), 0)
    # print("fileno:", f.fileno())
    # print(mm.readline())
    # print(mm[:5])
    # print(mm[6:])
    # mm.seek(0)
    # print(mm.readline())
    # mm.close()
    location = mm.find(b"2")
    print(location)
    print(mm.readline())
    lineThis = mm.rfind(b'\n', 0, location)
    print(lineThis)
    mm.seek(lineThis + 1)
    mm.readline()
    linelen = len(mm.readline())
    print(mm.tell())
    print(mm[lineThis + 1: mm.tell()])
    mm.move(lineThis + 1, mm.tell() - linelen, linelen)


    











#################################################################
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


# mm = mmap.mmap(-1, 14)
# mm.write(b"Hello world!")
# pid = os.getpid()
# print(pid)
# # if pid == 0:
# #     mm.seek(0)
# #     print(mm.readline())
# #     mm.close()
# mm.seek(0)
# print(mm.readline())
# mm.close()