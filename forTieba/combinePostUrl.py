#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os, mmap
from datetime import datetime, date, time
from getItemData import getDateTime, reverse, path

fill = b"+"

def deleteOldItem(old, new):
    with open(old, "r+b") as allF:
        allmm = mmap.mmap(allF.fileno(), 0)
        with open(new, "r+b") as newF:
            for line in newF:
                number = line.split(b"'")[1]
                allmm.seek(0)           
                location = allmm.find(number)
                if location > 0:
                    lineThis = allmm.rfind(b'\n', 0, location) + 1
                    allmm.seek(lineThis)
                    lens = len(allmm.readline()) - 2
                    allmm.seek(lineThis)
                    allmm.write(fill * lens)
        allmm.close()
                
def gatherItem(old, new):
    with open(old, "r+b") as allF:
        allmm = mmap.mmap(allF.fileno(), 0)
        allmm.seek(0)
        dest = allmm.find(fill)
        while dest > 0:    # only for first test
            src = allmm.find(b"[", dest)
            if src < 0:
                allmm.close()
                return dest
            dest2 = allmm.find(fill, src)
            if dest2 < 0:
                allmm.seek(-1, 2)
                count = allmm.tell() - src + 1
                allmm.close()
                return copyItem(allmm, dest, src, count)
            else:
                count = dest2 - src
            end = copyItem(allmm, dest, src, count)
            dest = end

def copyItem(mmap, dest, src, count):
    mmap.move(dest, src, count)
    mmap.seek(dest + count)
    mmap.write(fill * (src - dest))
    return dest + count

def combineUrls(old, new):
    deleteOldItem(old, new)
    end = gatherItem(old, new)
    reverse(new, new)
    with open(allfile, "r+b") as allF:
        data = allF.read()
        allF.seek(end)
        with open(newfile, "r+b") as newF:
            data2 = newF.read()
            allF.write(data2)

if __name__ == '__main__':
    allfile = os.path.join(path, "posts.rtf")
    newfile = os.path.join(path, "new.rtf")
    combineUrls(allfile, newfile)
