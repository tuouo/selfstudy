#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from PIL import Image
import os
im = Image.open("1L20.png")
w, h = im.size

white, data1, data2 = 255, [], []
for i in range(0, h, 20):
    pre, black, thisLine = 0, False, []
    for j in range(0, w, 20):
        if im.getpixel((j, i)) != white:
            if not black:
                black = True
                pre = j
        else:
            if black:
                black = False
                thisLine.append((j - pre) // 20)
    print(thisLine)
    data1.append(thisLine)

for i in range(0, w, 20):
    pre, black, thisLine = 0, False, []
    for j in range(0, h, 20):
        if im.getpixel((i, j)) != white:
            if not black:
                black = True
                pre = j
        else:
            if black:
                black = False
                thisLine.append((j - pre) // 20)
    print(thisLine)
    data2.append(thisLine)

data1 = data1[4:-4]
data2 = data2[4:-4]
# print(data1)

path = os.path.join(os.getcwd(), "data.rtf")
with open(path, "a") as f:
    f.write("%s %s\n" % (len(data1), len(data1)))
    for i in data1:
        f.write("%s\n" % str(i))
    for i in data2:
        f.write("%s\n" % str(i))

