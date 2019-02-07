# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(shenxianjun)s

#E_mail: shenxianjun.patrick@gmail.com

"""

'''
1.将切词后的内容变为一个list

'''
import jieba
content = "每天起床第一句，先给自己打个气，每次多吃一粒米，都要说声对不起，魔镜魔镜看看我，我的锁骨在哪里，美丽 我要美丽 我要变成万人迷"
segs_5 = jieba.lcut(content)
print(segs_5)

segs_5


'''
2.词性标注

'''

import jieba.posseg as psg
print([(x.word,x.flag) for x in psg.lcut(content)])


'''
3.专有名词导入词典

'''

txt = "铁甲网是中国最大的工程机械交易平台。"
print(jieba.lcut(txt))



jieba.add_word("铁甲网")
print(jieba.lcut(txt))



'''
4.批量导入词典

'''

jieba.load_userdict('user_dict.txt')
print(jieba.lcut(txt))