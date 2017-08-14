# -*- coding: UTF-8 -*-
'''
   有关list（列表）的相关知识点，它类似于数组
   但远比数组强大，可以多种类型混合使用
'''
list1 = [ 'runopp' , "hah" , 45 , 'ads' , 34.78]
list2 = [ 'nextList' , 23 , 5.6]
print list1
print list1[2]
print list1[2:]
print list1[1:4]
print list2 * 2
print list1 + list2
list1[3] = 23
print list1
