# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(shenxianjun)s

#E_mail: shenxianjun.patrick@gmail.com

"""

#常用数据分析技巧
import math

def get_log(x):
    # 普通写法
    if x > 0:
        y = math.log(x)
    else:
        y = float('nan')
    return y

get_log(15)

x=1
math.log(x) if x>0 else float('nan')

#1000以内的偶数

x=range(1000)
y=[item for item in x if item%2==0  ]



#dictionary

d = {'小象学院': 'http://www.chinahadoop.cn/',
    '百度': 'https://www.baidu.com/',
    '阿里巴巴': 'https://www.alibaba.com/',
    '腾讯': 'https://www.tencent.com/'}


print('通过key获取value: ', d['小象学院'])

for key,value in d.items():
    print('网站名臣是{}，网站URL是{}'.format(key,value))




#set

print('创建set:')
my_set = {1, 2, 3}
print(my_set)
my_set = set([1, 2, 3, 2])
print(my_set)

print('添加单个元素:')
my_set.add(3)
print('添加3', my_set)

my_set.add(4)
print('添加4', my_set)

print('添加多个元素：')
my_set.update([4, 5, 6])
print(my_set)


my_set.update((5,6,7))




#collections

import collections

c1 = collections.Counter(['a', 'b', 'c', 'a', 'b', 'b'])
c2 = collections.Counter({'a':2, 'b':3, 'c':1})
c3 = collections.Counter(a=2, b=3, c=1)

print(c1)
print(c2)
print(c3)

c3._replace(a=15)


help(collections)



p = Point(x=11, y=22)


#replace sonethings in collections.nametuple
import collections
employee = collections.namedtuple('emp','name, age, empid')

record1 = employee("shankar", 28, 12365 )



print "Record is ", record1
print "\n"
print  record1._replace(age= 25)
print "\n"
print "Record is ", record1
print "\n"
record1 = record1._replace(age= 25)
print "Record is ", record1


strings='in the meanwhile i am so sad ,because of my teeth'


collections.Counter(strings)

lists={}
for string in strings:
    if string not in lists:
        lists[string]=1
    else:
        lists[string]+=1
lists

sorted(lists.items(),key=lambda d:d[1],reverse=True)


#map functions

import math

print('示例1，获取两个列表对应位置上的最小值：')
l1 = [1, 3, 5, 7, 9]
l2 = [2, 4, 6, 8, 10]
mins = map(min, l1, l2)
print(mins)

# map()函数操作时，直到访问数据时才会执行
for item in mins:
    print(item)

print('示例2，对列表中的元素进行平方根操作：')
squared = map(math.sqrt, l2)
print(squared)
print(list(squared))



#lambda&map
# my_func = lambda a, b, c: a * b
# print(my_func)
# print(my_func(1, 2, 3))

# 结合map
print('lambda结合map')
l1 = [1, 3, 5, 7, 9]
l2 = [2, 4, 6, 8, 10]
result = map(lambda x, y: x * 2 + y, l1, l2)
print(list(result))
