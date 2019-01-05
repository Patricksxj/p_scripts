# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(shenxianjun)s

#E_mail: shenxianjun.patrick@gmail.com

"""

# -*- coding: utf-8 -*-
import json
import re
import jieba
from collections import Counter

class StatWords(object):
        def statTopN(self,path, n):
                file = open(path,'r')
                wordDict = {}
                content = file.read()
                wordlist = re.split('[\s\ \\,\;\.\!\n]+', content)
                for word in wordlist:
                        if word in wordDict:
                                wordDict[word]=wordDict[word]+1
                        else:
                                wordDict[word] = 1
                count = Counter(wordDict)
                print json.dumps(count.most_common()[:n], encoding="UTF-8", ensure_ascii=False)

STOPWORDS = [u'的', u'地', u'得', u'而', u'了', u'在', u'是', u'我', u'有', u'和',
u'就',  u'不', u'人', u'都', u'一', u'一个', u'上', u'也', u'很', u'到', u'说', u'要',
 u'去', u'你',  u'会', u'着', u'没有', u'看', u'好', u'自己', u'这']
PUNCTUATIONS = [u'。', u'，', u'“', u'”', u'…', u'？', u'！', u'、', u'；', u'（',
u'）',u'?',u'：']
#黑名单
f_in = open('file_in.txt')
f_out = open('file_out.txt', 'w')
#f_in原文档，f_out分词后的文档
try:
    for l in f_in:
        seg_list = jieba.cut(l)
        # print "/".join(seg_list)

        for seg in seg_list:
            if seg not in STOPWORDS and seg not in PUNCTUATIONS:
                f_out.write(seg.encode('utf-8', 'strict') + "\n")

finally:
    f_in.close()
    f_out.close()

if __name__ == '__main__':
       s = StatWords()
       s.statTopN("file_out.txt",10)
