#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os, mmap
path = os.path.join(os.getcwd(), "resource", "zangnan")
# with open(os.path.join(path, "new.rtf"), "r+") as new:
#     with open(os.path.join(path, "old.rtf"), "w+") as old:
#         data = []
#         for i in new:
#             data.append(i)
#         for i in data[::-1]:
#             old.write(i)

def getLast():
    with open(os.path.join(path, "old.rtf"), "rb") as old:
        i = -1
        while i > -80:
            i = i - 1
            old.seek(i, 2)    # must be in rb mode
            if old.read(1) == b'\n':
                break
        data = old.read(-i)
        with open(os.path.join(path, "cache.rtf"), "wb") as cache:
            cache.write(data)
        with open(os.path.join(path, "cache.rtf"), "r") as cache:
            return cache.read()


# real = "['/p/4245040282', '中国最西端这座山叫啥', '2016-01-01 22:29:00']"
# print(real.encode('utf-8'))

data = getLast()
print(data)