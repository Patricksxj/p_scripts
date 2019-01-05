# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(shenxianjun)s

#E_mail: shenxianjun.patrick@gmail.com

"""

print("{}".format("hello"))

"{}".format("hello")



import os
os.curdir()

file=open('word.txt','r')
content=file.readline(limit=10)
print(content)
file2=open(r'C:\Users\Administrator\Desktop\new_word.txt','w')
content2=file2.write(content)
file.close()
file2.close()





通过readline输出，对于比较大的文件，这种占用内存比较小。
#coding:utf-8

f = open('word.txt','r')
result = []
for line in open('word.txt'):
    line = f.readline()
    result.append(line)
f.close()
open('result-readline.txt', 'w').write('%s' % '\n'.join(result))
