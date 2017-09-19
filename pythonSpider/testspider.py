# -*- coding:UTF-8 -*-
import urllib
import urllib2
import re
import  thread
import time


url = 'http://www.qiushibaike.com/hot/page/1'
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
headers = { 'User-Agent' : user_agent}

request = urllib2.Request(url,headers = headers)
response = urllib2.urlopen(request)
content = response.read().decode('utf-8')
#print content
pattern = re.compile('</h2.*?content">.*?<span>(.*?)</',re.S)
items = re.findall(pattern,content)
for item in items:
	print item.rstrip()

'''
url = 'http://wenku.baidu.com/list/63'
request = urllib2.Request(url)
response = urllib2.urlopen(request)
content = response.read().decode('gb2312')
pattern = re.compile('<div.*?id="tabContent".*',re.S)
items = re.findall(pattern,content)
pattern2 = re.compile('<tr.*?<a.*?href="/view/.*?title="(.*?)">',re.S)
items2 = re.findall(pattern2,items[0])
i = 1
for item in items2:
	print i,' ',item
	i+=1
#print content
'''

'''
class QSBK:

    def __init__(self):
        self.pageIndex = 1
        self.user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
        self.headers = {'User-Agent' :self.user_agent}
        self.stories = []
        self.enable = False

    def getPage(self,pageIndex):
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

    def getPageItems(self,pageIndex):
        pageCode = self.getPage(pageIndex)
        if not pageCode:
            print "page load error"
            return None
        pattern = re.compile('h2>(.*?)</h2.*?content">(.*?)</.*?number">(.*?)</',re.S)
        items = re.findall(pattern,pageCode)
        pageStories = []
        for item in items:
            pageStories.append([item[0].strip(),item[1].strip(),item[2].strip()])
        return pageStories

    def loadPage(self):
        if self.enable==True:
            if len(self.stories)<2:
                pageStories = self.getPageItems(self.pageIndex)
                if pageStories:
                    self.stories.append(pageStories)
                    self.pageIndex +=1

    def getOneStory(self,pageStories,page):
        for story in pageStories:
            input = raw_input()
            self.loadPage()
            if input == "Q":
                self.enable = False
                return
            print u"第%d页\t发布人：%s\t 赞：%s\n%s" %(page,story[0],story[2],story[1])

    def start(self):
        print u'正在读取，回车查看，Q退出'
        self.enable = True
        self.loadPage()
        nowPage = 0
        while self.enable:
            if len(self.stories)>0:
                pageStories = self.stories[0]
                nowPage +=1
                del self.stories[0]
                self.getOneStory(pageStories,nowPage)

spider = QSBK()
spider.start()

'''
