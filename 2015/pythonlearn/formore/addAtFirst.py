#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
path = os.path.join(os.getcwd(), "resource")
brtf = os.path.join(path, "b.rtf")
with open(brtf, 'w') as f:
    for i in range(5):
        f.write("Hello, this is line %s.\n" % (i * str(i)))

with open(brtf, 'r+') as f:
    data = f.read()
    f.seek(0)
    f.write("add" + "\n" + data)