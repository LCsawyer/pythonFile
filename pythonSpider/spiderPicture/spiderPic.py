# -*- coding:utf-8 -*-

import urllib
import urllib2
import re

def getContents(url,pageindex):
	urlpage = url + "?page=" + str(pageindex)
	request = urllib2.Request(urlpage)
	response = urllib2.urlopen(request)
	page = response.read().decode('gbk')
	pattern = re.compile('<img data-ks-lazyload="(.*?)" src',re.S)
	items = re.findall(pattern,page)
	return items

def setUrlFormat(url):
	urlFormat = "https:" + url
	return urlFormat

def saveImg(url,filName):
	u = urllib.urlopen(url)
	data = u.read()
	f = open(fileName, 'wb')
	f.write(data)
	f.close()


def setFilenameFormat(page,index):
	return "img/" + str(page) + "-" + str(index) + ".png"

def setFilenameFormat2(page,index):
	return "img/" + str(page) + "-" + str(index) + ".jpg"


#filename = "img/" + str(page) + ".png"
url = 'http://mm.taobao.com/json/request_top_list.htm'
for page in range(1,5):
	index = 1
	items = getContents(url,page)
	for item in items:
		if item[-3:] == "png":
			fileName = setFilenameFormat(page,index)
		else:
			fileName = setFilenameFormat2(page,index)
		urlimg = setUrlFormat(item)
		saveImg(urlimg,fileName)
		print "aveimg",index
		index += 1		


























