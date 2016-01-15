#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from PIL import Image
from urlParser import urlPostParser, pageNumParser
import urllib.request as ur, os, re, time

def getAllComment(url, post_id):
    localTime = str(int(time.time()))
    commentUrl = "http://tieba.baidu.com/p/totalComment?t="
    commentURL = "%s%s&tid=%s&fid=%s&pn=1&see_lz=0" % (commentUrl, localTime, url.split('/')[-1], post_id)
    req = ur.urlopen(commentURL)
    data = req.read().replace(b'"', b'').decode("unicode_escape")
    return getEachComment(data)

def getEachComment(data):
    post_id    = re.findall("post_id:(\d+),comment_id", data)
    comment_id = re.findall("comment_id:(\d+),username", data)
    username   = re.findall("username:(\S+?),user_id", data)    # need "?""
    content    = re.findall("content:(.+?),ptype", data)
    return [post_id, comment_id, username, content]

def writeContent(allContent, url, path, filename):
    one_post_id = allContent[0][0].split(", ")[3]
    comment = getAllComment(url, one_post_id)
    with open(os.path.join(path, filename), "ab") as f:
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
    
def getOnePost(url, path):      
    url += "?pn="
    data = ur.urlopen(url + "1").read().decode('utf-8', 'ignore')
    numParser = pageNumParser()
    numParser.feed(data)
    pageNum = numParser._num
    for page in range(pageNum):    	
        response = ur.urlopen(url + str(page + 1))
        data = response.read()
        data = data.decode('utf-8', 'ignore')
        parser = urlPostParser()
        parser.feed(data)
        print("get page %s ok." % (page + 1))
        if parser._all:
            print("write all.")
            writeContent(parser._all, url, path, "text.rtf")
        if parser._img:
            print("write img.")
            for name, urlIm in parser._img.items():
            	if not os.path.exists(os.path.join(path, name)):
                    with open(os.path.join(path, name), "wb") as img:                    
                       img.write(ur.urlopen(urlIm).read())

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
