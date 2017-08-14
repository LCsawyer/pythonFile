# -*- coding: UTF-8 -*-
'''
x = 'there are %d types of people.' % 4
binary = "binary"
do_not = "don't"
y = "those who know %s and those who %s." % (binary , do_not)

print x
print y

print "i said:%r" %x # %r打印所有的，显示变量的原始数据(数字和字符均可)，%s打印出的更符合可读性
print "i also: '%s'." %y

hl = False
joke = "isn't that joke so funny ? %s"
print joke %hl
'''
'''
format = '%r %r %r %r'

print format % (1,2,3,4)
print format % ('one' , 'two' , 'three' , 'four')
print format % (True , True , False , False)
print format % (format , format , format , format)
print format % ("i'm sawyer." , "i'm bob" , "i'm james" , "i'm lee")
print 'i %s df' %34
#print 'i %d df' %'asdd' 数字可使用%s 但字符不可用%d
print 'ok %r asd' %"saw'y'er"
'''
"""
months = "Jan\nFeb\nMar\nApr\nMay\n"
print 'here are the months',months
print '''
there add
asf
sdghj ffdgh 
gfg
'''
"""
while True:
  for i in ["/" , "-" , "|" , "\\" , "|"]:
     print "%s \r " % i, 