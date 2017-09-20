# -*- coding:utf-8 -*-

import urllib
import urllib2
import re
import sys
from bs4 import BeautifulSoup
fileout = open('spider.txt','w+')
sys.stdout = fileout
urlpage = "http://iask.sina.com.cn/c/187.html"
def getPage(urlpage):
	request = urllib2.Request(urlpage)
	response = urllib2.urlopen(request)
	return response.read()#.decode('utf-8')
	
page = getPage(urlpage)
soup = BeautifulSoup(page,'html5lib')
items = soup.find_all(class_="question-title")

def getAnswyer(page):
	soup = BeautifulSoup(page,'html5lib')
	items = soup.select('.answer_text > div > span > pre')
	return items[0].string.encode('UTF-8')

print "这是一个简单的spider测试\n"
count = 1
for item in items:
	
	print "问题"+str(count)+"："
	qustion = item.a.string.encode('UTF-8')
	print qustion , '\n'
	url = "http://iask.sina.com.cn" + str(item.a['href'])
	print "最佳回答："
	print getAnswyer(getPage(url)).strip() + '\n'
	print "----------------------------------------\n"
	count += 1




fileout.close()







