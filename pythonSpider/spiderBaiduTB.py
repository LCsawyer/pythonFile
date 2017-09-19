# -*- coding:utf-8 -*-

import urllib
import urllib2
import re
import codecs

class Bdtb(object):
	def __init__(self,seelz):
		self.baseurl = "https://tieba.baidu.com/p/3138733512?see_lz="
		self.seelz = seelz
		self.wfile = None
		self.floor = 1
		self.defaultTitle = "百度贴吧"
		#self.pageNum = 0
		
	def getPage(self,pageIndex):
		url = self.baseurl + str(self.seelz) + "&pn=" + str(pageIndex)
		try:
			request = urllib2.Request(url)
			response = urllib2.urlopen(request)
			#return response.read().decode('utf-8')
			#由于输出的文件也是utf-8的所以无需编解码，不过一般使用编解码通用性更好
			return response.read()
		except urllib2.URLError, e:
			if hasattr(e,"reason"):
				print u"连接百度贴吧失败,错误原因",e.reason
				return None

	def getTitle(self):
		pageCode = self.getPage(1)
		patterns = re.compile('<h3.*?>(.*?)</h3>',re.S)
		searchTitle = re.search(patterns,pageCode)
		items = searchTitle.group(1)
		if len(items) > 0:
			return items.strip()
		else:
			return None
	def setFileName(self):
		gt = self.getTitle()
		if gt != None:
			filename = gt + ".txt"	
		else:
			filename = self.defaultTitle + ".txt"
		#self.wfile = codecs.open(filename,'w+','UTF-8')
		self.wfile = open(filename,'w+')

	def getPageNum(self):
		pageCode = self.getPage(1)
		patterns = re.compile('<li class="l_reply_num.*?<span.*?span>.*?<span.*?>(.*?)</span',re.S)
		searchNum = re.search(patterns,pageCode)
		pagenum = searchNum.group(1)
		return int(pagenum.strip())

	def getContent(self,pageIndex):
		pagecode = self.getPage(pageIndex)
		patterns = re.compile('<div id="post_content.*?">(.*?)</div>',re.S)
		items = re.findall(patterns,pagecode)
		contents = []
		for item in items:
			content = '\n' + self.processContent(item) + '\n'
			#contents.append(content.encode('UTF-8'))
			contents.append(content)
		return contents

	def processContent(self,content):
		removeimg = re.compile('<img.*?">',re.S)
		removealigin = re.compile('<a href.*?">',re.S)
		content = re.sub(removeimg,'',content)
		content = re.sub('<br>','\n',content)
		content = re.sub(removealigin,'',content)
		content = re.sub('</a>','',content)
		return content.strip()
	
	def writeContent(self,contents):
		for content in contents:
			tag0 = str(self.floor) + '----------------------------------------------\n'
			self.wfile.write(tag0)
			self.wfile.write(content)
			self.floor += 1

	def start(self):
		self.setFileName()
		for index in range(1,self.getPageNum() + 1):
			print u'正在输出第',index,'层'
			contents = self.getContent(index)
			self.writeContent(contents)
			#self.wfile.write(u'下一层\n')
		self.wfile.close()



bt = Bdtb(1)
bt.start()
#print bt.getPageNum()
'''
file1 = codecs.open('我是.txt','w+','UTF-8')
for content in bt.getContent(1):
	file1.write(content)

file1.close()
'''














