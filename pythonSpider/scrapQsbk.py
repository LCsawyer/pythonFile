# -*- coding:utf-8 -*-

import urllib
import urllib2
import re
import codecs

class Qsbk(object):
	def __init__(self):
		self.headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
		self.pageIndex = 1
		self.stories = []
		self.enable = False
		self.openfile = None

	def getpage(self,pageIndex):
		try:
			url = 'http://www.qiushibaike.com/hot/page/' + str(pageIndex)
            		request = urllib2.Request(url,headers=self.headers)
            		response = urllib2.urlopen(request)
            		pageCode = response.read().decode('utf-8')
            		return pageCode
		except urllib2.URLError,e:
			if hasattr(e,"reason"):
               			print "error",e.reason
                		return None

	def getpageItem(self,page):
		pagecode = self.getpage(page)
		if not pagecode:
			print "页面加载失败....."
			return None
		
		pattern = re.compile('<h2>(.*?)</h2.*?content">.*?<span>(.*?)</.*?number">(.*?)</i>',re.S)
		#pattern = re.compile('h2>(.*?)</h2.*?content">(.*?)</.*?number">(.*?)</',re.S)
		items = re.findall(pattern,pagecode)
		pageStories = []
		for item in items:
			pageStories.append([item[0].strip(),item[1].strip(),item[2].strip()])
		return pageStories
	def loadpage(self):
		if self.enable == True:
			if len(self.stories) < 2:
				pagestories = self.getpageItem(self.pageIndex)
				if pagestories:
					self.stories.append(pagestories)
					self.pageIndex += 1
	def collectStories(self,pagestories,page):
		for story in pagestories:
			input = raw_input()
			self.loadpage()
			if input == "Q":
				self.enable = False
				return
			test = story[1].strip()	
			test = re.sub('<br/>','',story[1])		
			print u"第%d页 发布人：%s 赞：%s" %(page,story[0],story[2])
			self.openfile.write(u"第%d页 发布人：%s 赞：%s \n%s\n" %(page,story[0].strip(),story[2].strip(),test))
			#self.openfile.write(test)
	def start(self):
		print u'正在读取，回车开始，Q退出'
		self.openfile = codecs.open('qsbk.txt','a','UTF-8')
		self.enable = True
		self.loadpage()
		nowpage = 0
		while self.enable:
			if len(self.stories)>0:
                		pageStories = self.stories[0]
               			nowpage +=1
                		del self.stories[0]
                		self.collectStories(pageStories,nowpage)
		self.openfile.close()

spider = Qsbk()
spider.start()






















		
