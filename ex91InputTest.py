# -*- coding: UTF-8 -*-


age = raw_input("How old are you?") #raw_input的含义表示输入一个字符串（无论你输入什么都被当成字符串）
print "how tall are you?",          #因为它返回的是字符串，他可以有字符串作为参数
height = raw_input()                #其含义和标注1差不多
print "how much do you weigh?",     #标注1
weight = raw_input()
print "so you are %s old , %s tall and %s heavy." %(age , height , weight)
print height
