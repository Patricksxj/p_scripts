# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(shenxianjun)s

#E_mail: shenxianjun.patrick@gmail.com

"""

jieba.add_word('魏无羡','蓝曦臣')

import sys

import jieba
import jieba.analyse
wf = open('clean_data.txt','w+')
for line in open(r'魔道祖师-墨香铜臭.txt',encoding='utf-8'):
    item = line.strip('\n\r').split('\t')# print item[1]
    tags = jieba.analyse.extract_tags(item[0])#jieba分词
    tagsw = ",".join(tags)#逗号连接切分的词
    wf.write(tagsw)
wf.close()




word_lst = []
word_dict= {}
stopwords = [line.rstrip() for line in open('stop_words.txt')]
with open(r'clean_data.txt') as wf,open("word.txt",'w') as wf2:
    for word in wf:
        word_lst.append(word.split(','))# //使用逗号进行切分
        for item in word_lst:
            for item2 in item:
                #print(item2)
                if item2 not in stopwords and item2 not in ('魏无羡','含光君','蓝曦臣'):
                    if item2 not in word_dict:#//统计数量
                        word_dict[item2] = 1
                    else:
                        word_dict[item2] += 1
                else:
                    pass
    for key in word_dict:
        #print(key,word_dict[key])
        wf2.write(key+' '+str(word_dict[key])+'\n')




word_dict2=sorted(word_dict.items(), key = lambda  d:d[1],reverse=True)

word_dict2[:500]
