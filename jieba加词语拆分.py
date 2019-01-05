# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(shenxianjun)s

#E_mail: shenxianjun.patrick@gmail.com

"""

import jieba

seg_list = jieba.cut("今天在Starbucks点了一杯拿铁", cut_all=False)
print("Default Mode: " + "/ ".join(seg_list))  # 精确模式


jieba.add_word('大新区', freq=None, tag=None)


print(seg_list)





import jieba.posseg as pseg
words = pseg.cut("北京大新区环卫有限公司")
new_list=[]
for w in words:
    new_list.append(w.word)

new_list