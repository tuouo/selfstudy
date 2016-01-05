#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
path = os.path.join(os.getcwd(), "resource")
artf = os.path.join(path, "a.rtf")
with open (artf, 'w') as f:
    print(len("Hello, this is line %s." % '?'))
    for i in range(5):
        f.write("Hello, this is line %s.\n" % i)
        print(len("Hello, this is line %s.\n" % i), f.tell())        
        # why f.tell() = len(context) + 1 in first line and similar in after 
        # ? \r\n ?  maybe


with open (artf, 'rb') as f:
    for i in f:
        print(i)


with open (artf, 'r') as f:
    print(f)
    for line in f:
        print(line, end = '')
    print(f.tell())
    f.seek(0)
    print("1:", f.read(1), len(f.read(1)))
    print("10:", f.read(12), len(f.read(12)))
    f.seek(0)
    print(f.read(48), "----0")
    f.seek(1)
    print(f.read(47), "----1")
    f.seek(21)
    print(f.read(27), "----21")
    f.seek(22)
    print(f.read(26), "----22")
    f.seek(23)
    print(f.read(25), "----23")    # why start same as f.seek(22)
    f.seek(24)                     # ? \r\n ?  maybe
    print(f.read(24), "----24")

with open (artf, 'a') as f:
    f.write("Hello, this is append line.")

# ###################################################################
# with open (artf, 'r+') as f:        # a
#     f.write("This is r+ line.\n")
#     for line in f:
#         print(line)

# with open (artf, 'r+') as f:        # b
#     for line in f:                  # This is does same thing as a.
#         print(line)
#     f.write("This is r+ line.\n")
# ###################################################################

with open (artf, 'r+') as f:
    f.write("This is r+ line.\n")

with open (artf, 'w+') as f:
    f.write("This is r+ line.\n")