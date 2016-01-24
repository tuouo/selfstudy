#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from PIL import Image
from urlParser import urlPostParser, pageNumParser
import urllib.request as ur, urllib.error as ue, os, re, time, difflib, socket

def getAllComment(url, post_id):
    localTime = str(int(time.time()))
    commentUrl = "http://tieba.baidu.com/p/totalComment?t="
    commentURL = "%s%s&tid=%s&fid=%s&pn=1&see_lz=0" % (commentUrl, localTime, url.split('/')[-1], post_id)
    req = ur.urlopen(commentURL)
    data = req.read().replace(b'"', b'').decode("unicode_escape")
    return getEachComment(data)

def getEachComment(data):
    post_id    = re.findall("post_id:(\d+),", data)
    comment_id = re.findall("comment_id:(\d+),", data)
    username   = re.findall("username:(\S+?),", data)    # need "?""
    content    = re.findall("content:(.+?),", data)
    return [post_id, comment_id, username, content]

def writeContextFirstTime(allContent, url, filename):
    one_post_id = allContent[0][0].split(", ")[3]
    comment = getAllComment(url, one_post_id)
    with open(filename, "ab") as f:
        for i in allContent:
            one_post_id = i[0].split(", ")[3]
            for j in i:
                f.write(j.encode('utf-8') + b"\r\n")     # reply
            num, maxNum = 0, len(comment[0])
            while num < maxNum and one_post_id == comment[0][num]:
                context = comment[3][num].replace(r"<\/a>", "").replace(r"\/", r"/")
                for i in re.findall("(<a.+>)", context): # remove href for name
                    context = context.replace(i, "")             
                data = "*%s*%s:%s" % (comment[1][num], comment[2][num], context)
                f.write(data.encode('utf-8') + b"\r\n")  # comment
                num += 1
            f.write(b"\r\n")

def writeContent(allContent, url, path, firstTime):
    filetext = os.path.join(path, "text.rtf")
    if firstTime:
        if os.path.exists(filetext):
            os.remove(filetext)
        writeContextFirstTime(allContent, url, filetext)
    else:
        filecache = os.path.join(path, "cache.rtf")
        writeContextFirstTime(allContent, url, filecache)
        combineFile(filecache, filetext)

def combineFile(filecache, filetext):
    data, data1, data2 = [], [], []
    with open(filecache, "r+", encoding = "utf-8") as f1:
        data1 = f1.readlines()
    with open(filetext, "r+", encoding = "utf-8") as f2:
        data2 = f2.readlines()
    if data1 == data2:
        return
    result = list(difflib.ndiff(data1, data2))
    for row in result:    
        if row[0] != "?":
            data.append(row[2:])
    with open(filetext, "w+") as f:
        for i in data:
            f.write(i)

def getOnePost(url, path, firstTime):      
    url += "?pn="
    timeout = 20
    socket.setdefaulttimeout(timeout)
    response = ur.urlopen(url + "1")
    data = response.read()
    response.close()
    data = data.decode('utf-8', 'ignore')
    numParser = pageNumParser()
    numParser.feed(data)
    pageNum = numParser._num
    for page in range(pageNum):    	
        response = ur.urlopen(url + str(page + 1))
        data = response.read()
        response.close()
        data = data.decode('utf-8', 'ignore')
        parser = urlPostParser()
        parser.feed(data)
        print("get page %s ok." % (page + 1))
        if parser._all:
            print("write all.")
            writeContent(parser._all, url, path, firstTime)
        if parser._img:
            print("write img.")
            for name, urlIm in parser._img.items():
                if not os.path.exists(os.path.join(path, name)):
                    with open(os.path.join(path, name), "wb") as img:   
                        try:
                            data = ur.urlopen(urlIm).read()
                            img.write(data)
                            time.sleep(1)
                        except ue.URLError as eu:
                            # with open(os.path.join(path, "error.rtf"), "a") as feu:
                            #     feu.write("%s, %s\n" % (name, urlIm))
                            pass
                        except ue.HTTPError as eh:
                            # with open(os.path.join(path, "error.rtf"), "a") as feh:
                            #     feh.write("%s, %s\n" % (name, urlIm))
                            pass

        print("Write page %s ok." % (page + 1))
        time.sleep(1)


if __name__ == '__main__':
    # url = "http://tieba.baidu.com/p/4147438587" #in this post, last page has nothing
    url = "http://tieba.baidu.com/p/3586361872"
    fileName = re.findall("/(\d+)", url)[0]
    path = os.path.join(os.getcwd(), "resource", "zangnan")
    filepath = os.path.join(path, fileName)
    if not os.path.exists(filepath):
        os.mkdir(filepath)
    print("****    %s    ****" % url)
    getOnePost(url, filepath)
    print("OK, %s" % url)
