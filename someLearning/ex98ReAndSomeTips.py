# -*- coding: UTF-8 -*-

import re

line = "cats are smarter than dogs"
'''
#matchoj = re.match('(.+) are (.*?) dogs',line) #match()中的第一个参数表示匹配模式
matchoj = re.match('.*?',line) #本例中其实它就是匹配了一整个字串，然后将字符串拆分
#matchoj = re.match('...',line)  #‘（）’表示分组，‘.’表示匹配除\n外的所有字符,一个就代表匹配一个字符
print matchoj.group()         #‘*’代表重复前面字符0-无穷次，‘+’是1-无穷，‘？’代表非贪婪模式 '''                             #例如‘.*a’代表一直匹配到a字符之前，如果没有‘a’这个断点，那么‘.*’就会
                              #匹配整个字符串，而‘.*?’就会选择0-无穷中的0次（默认是贪婪模式，所以
                              #‘.*’会选择无穷次）
'''                           
line = 'abbbc'
matchoj = re.match('ab*',line)
matchoj2 = re.match('ab*?',line)
print matchoj.group()
print matchoj2.group()
'''

'''
	匹配模式中后加‘*’和加‘+’的区别，定义上的区别前面已讲，在上例中似乎他们的区别不大，但是比如说
line = 'adff' ; re.match('\d*',line)不返回None，既可以匹配，但把‘*’换成‘+’就不行了，一个可以无字符
一个必须至少有一个(如下例)
'''

matchoj = re.match('\d*',line)
matchoj2 = re.match('\d+',line)

if matchoj == None :
	print 'no match'
if matchoj2 == None:
	print 'matchoj2 no match'
