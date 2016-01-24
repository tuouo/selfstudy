#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from getPostUrl import getALLPostUrl, getNewPostUrl
from getEachNewUrl import getOnePost
from combinePostUrl import combineUrls
import os, re, socket

lastPage = 130
path = os.path.join("C:/", "resource", "TiebaCrawler", "zangnan")
url = "http://tieba.baidu.com/f?kw=%E4%BC%AA%E9%98%BF%E9%B2%81%E7%BA%B3%E6%81%B0%E5%B0%94%E9%82%A6&ie=utf-8&pn="
allUrlFile = os.path.join(path, "postUrlItem.rtf")
newUrlFile = os.path.join(path, "newUrlItem.rtf")

def fromUrlItemGetPost(path, itemFile, firstTime):
    with open(itemFile, "rb+") as f:
        for line in f:
            url = line.split(b"'")[1].decode('utf-8')
            fileName = re.findall("/(\d+)", url)[0]
            filepath = os.path.join(path, fileName)
            if not os.path.exists(filepath):
                os.mkdir(filepath)
            url = "http://tieba.baidu.com" + url
            print("****    %s    ****" % url)
            # firstTime = False if os.path.exists(os.path.join(path, "text.rtf")) else True            
            try:
                getOnePost(url, filepath, firstTime)
            except socket.timeout:

                getOnePost(url, filepath, firstTime)
            print("OK, %s" % url)
    

if __name__ == "__main__":
    if not os.path.exists(path):
        os.makedirs(path)
    if not os.path.exists(allUrlFile):
        getALLPostUrl(allUrlFile, url, lastPage -1)
        fromUrlItemGetPost(path, allUrlFile, True)
    
    fromUrlItemGetPost(path, allUrlFile, True)

    # getNewPostUrl(allUrlFile, newUrlFile, url)
    # fromUrlItemGetPost(path, newUrlFile)
    # combineUrls(allUrlFile, newUrlFile)
