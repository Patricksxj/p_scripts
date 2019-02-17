
# coding: utf-8

# # 用gensim学习word2vec 
# 
# https://www.cnblogs.com/pinard/p/7278324.html

# In[131]:


import os
os.getcwd()
os.chdir(r'D:\P_WORKPLACE')
print(os.getcwd())


# In[330]:


import jieba
import jieba.analyse
jieba.suggest_freq('沙瑞金', True)
jieba.suggest_freq('田国富', True)
jieba.suggest_freq('高育良', True)
jieba.suggest_freq('侯亮平', True)
jieba.suggest_freq('钟小艾', True)
jieba.suggest_freq('陈岩石', True)
jieba.suggest_freq('欧阳菁', True)
jieba.suggest_freq('易学习', True)
jieba.suggest_freq('王大路', True)
jieba.suggest_freq('蔡成功', True)
jieba.suggest_freq('孙连城', True)
jieba.suggest_freq('季昌明', True)
jieba.suggest_freq('丁义珍', True)
jieba.suggest_freq('郑西坡', True)
jieba.suggest_freq('赵东来', True)
jieba.suggest_freq('高小琴', True)
jieba.suggest_freq('赵瑞龙', True)
jieba.suggest_freq('林华华', True)
jieba.suggest_freq('陆亦可', True)
jieba.suggest_freq('刘新建', True)
jieba.suggest_freq('刘庆祝', True)
jieba.suggest_freq('光明峰', True)


# In[331]:


class MySentences(object):
    def __init__(self, fname):
        self.fname = fname

    def __iter__(self):
        for line in open(self.fname, 'r',encoding='utf-8'):
            yield line.split()


# In[350]:


sentences = MySentences('./in_the_name_of_people.txt')
list(sentences)[:10]


# In[343]:


STOP_WORDS = set([w.strip() for w in open("./stop_words.txt").readlines()])
STOP_WORDS=list(STOP_WORDS)


# In[351]:


sentences = list(MySentences('./in_the_name_of_people.txt'))


# In[352]:


for idx, sentence in enumerate(sentences):
    for line in sentence:
        words=jieba.lcut(line,HMM=True)
        sentence = [w for w in words if w not in STOP_WORDS]
        sentences[idx] = sentence


# In[ ]:


sentences[:10]


# In[ ]:


# import modules & set up logging
import logging
import os
from gensim.models import word2vec

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

model = word2vec.Word2Vec(sentences, hs=0,min_count=1,window=4,workers = 4,size=100)  


# In[369]:


req_count = 5
for key in model.wv.similar_by_word('逃跑', topn =100):
    if len(key[0])==3:
        req_count -= 1
        print(key[0], key[1])
        if req_count == 0:
            break;


# In[370]:


req_count = 5
for key in model.wv.similar_by_word('政绩', topn =100):
    if len(key[0])==3:
        req_count -= 1
        print(key[0], key[1])
        if req_count == 0:
            break;


# In[373]:


req_count = 5
for key in model.wv.similar_by_word('反腐败', topn =100):
    if len(key[0])==3:
        req_count -= 1
        print(key[0], key[1])
        if req_count == 0:
            break;


# In[374]:


req_count = 5
for key in model.wv.similar_by_word('沙瑞金', topn =100):
    if len(key[0])==4:
        req_count -= 1
        print(key[0], key[1])
        if req_count == 0:
            break;


# In[378]:


req_count = 5
for key in model.wv.similar_by_word('医院', topn =100):
    if len(key[0])==2:
        req_count -= 1
        print(key[0], key[1])
        if req_count == 0:
            break;


# In[172]:


print(model.wv.similarity('沙瑞金', '高育良'))
print(model.wv.similarity('李达康', '王大路'))


# In[379]:


print(model.wv.doesnt_match("沙瑞金 高育良 李达康 钟小艾".split()))


# In[ ]:




