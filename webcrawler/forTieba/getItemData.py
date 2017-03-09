#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from datetime import datetime
import os

def getDateTime(item, isItem = False):
    if item.find(":") < 0 and item.find("-") < 0:        
        return None
    data = item.split("'")[5] if isItem else item
    if data.find(":") < 0:
        today = datetime.today()
        dt = datetime(today.year, int(data.split("-")[0]), int(data.split("-")[1]))
        if today < dt:
            dt = dt.replace(year = today.year - 1)
        return dt
    else:
        return datetime.strptime(data, "%Y-%m-%d %H:%M:%S")

def getLastData(fileName):
    with open(fileName, "rb") as one:
        if sum(1 for x in one) == 1:
            one.seek(0)
            return one.readline()
    with open(fileName, "rb") as old:
        i = -1
        while True:
            i = i - 1
            old.seek(i, 2)    # must be in rb mode            
            if old.read(1) == b'\n':
                datas = old.read(-i).split(b'\n')[0].split(b"'")
                if len(datas) > 5:
                    return datas[5].decode('utf-8')

def reverse(oldfile, newfile):
    data = []
    with open(oldfile, "r+b") as old:
        for i in old:
            data.append(i)
    with open(newfile, "w+b") as new:
        for i in data[::-1]:
            new.write(i)