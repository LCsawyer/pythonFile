# -*- coding: UTF-8 -*-

import re
'''
line = "202-53625-54#我只是想试试一些新功能//****"

num = re.sub(r'#.*$','',line) #原字符串不变，返回替换后的字符串
num2 = re.sub(r'\D','',line)
print num

print num2   
'''
'''
def doubl(matched):
	value = int(matched.group('value'))
	return str(value * 2)


s = 'a23b45cv567'

print (re.sub('(?P<value>\d+)',doubl,s))


s = '3456rt6'
matche = re.match('(?P<value>\d*)',s)
print matche.group('value')
'''

s = 'wertyu'
news = re.sub('\d*','2',s)
print news
