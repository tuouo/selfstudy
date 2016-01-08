#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from datetime import datetime, date, time
import os

path = os.path.join(os.getcwd(), "resource", "zangnan")
url = "http://tieba.baidu.com/f?kw=%E4%BC%AA%E9%98%BF%E9%B2%81%E7%BA%B3%E6%81%B0%E5%B0%94%E9%82%A6&ie=utf-8&tp=0&pn="

def getDateTime(item, isItem = False):
    # print(item)
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
    with open(os.path.join(path, fileName), "rb") as one:
        if sum(1 for x in one) == 1:
            one.seek(0)
            return one.readline()
    with open(os.path.join(path, fileName), "rb") as old:
        i = -1
        while True:
            i = i - 1
            old.seek(i, 2)    # must be in rb mode            
            if old.read(1) == b'\n':
                datas = old.read(-i).split(b'\n')[0].split(b"'")
                if len(datas) > 5:
                    return datas[5].decode('utf-8')

def reverse(old, new):
    oldfile = os.path.join(path, old)
    newfile = os.path.join(path, new)
    data = []
    with open(oldfile, "r+") as old:
        for i in old:
            data.append(i)
    with open(newfile, "w+") as new:
        for i in data[::-1]:
            new.write(i)