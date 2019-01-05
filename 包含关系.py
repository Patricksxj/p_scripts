# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(shenxianjun)s

#E_mail: shenxianjun.patrick@gmail.com

"""

#1.使用成员操作符 in

s='nihao,shijie'
t='nihao'
result = t in s
print(result)



#2.使用string模块的find()/rfind()方法


s='nihao,shijie'
t='nihao'
result =s.find(t)!=-1
print(result)
#True
result =s.rfind(t)!=-1
print(result)




#3.使用string模块的index()/rindex()方法
#index()/rindex()方法跟find()/rfind()方法一样，只不过找不到子字符串的时候会报一个ValueError异常。


def find_string(s,t):
    try:
        s.index(t)
        return True
    except(ValueError):
        return False

s='nihao,shijie'
t='nihao'
result = find_string(s,t)
print(result)
#True


#4.使用字符串对象的find()/rfind()、index()/rindex()和count()方法

s='nihao,shijie'
t='nihao'
result = s.find(t)>=0
print(result)
#True
result=s.count(t)>0
print(result)
#True
result=s.index(t)>=0
print result
#True