# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(shenxianjun)s

#E_mail: shenxianjun.patrick@gmail.com

"""



'''
1.hanLP分词

'''
from pyhanlp import *
content = "现如今，机器学习和深度学习带动人工智能飞速的发展，并在图片处理、语音识别领域取得巨大成功。"
print(HanLP.segment(content))





txt = "铁甲网是中国最大的工程机械交易平台。"
print(HanLP.segment(txt))


'''
2.hanLP加入自定义词典

'''


CustomDictionary.add("铁甲网")
CustomDictionary.insert("工程机械", "nz 1024")
CustomDictionary.add("交易平台", "nz 1024 n 1")
print(HanLP.segment(txt))