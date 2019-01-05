# -*- coding: utf-8 -*-
import pandas as pd
import jieba
import os
import numpy
os.chdir('D:\P_WORKPLACE')
# print(os.getcwd())
# path=r'G:\统计类知识与材料\唐宇迪\机器学习课程资料\机器学习算法配套案例实战\Python文本分析\搜狗新闻语料\val.txt'
#print(path)
df_news = pd.read_table('./val.txt',names=['category','theme','URL','content'],encoding='utf-8')
df_news = df_news.dropna()
print(df_news.shape)

contents=df_news.content.values.tolist()
print(contents[100])

contents_s=[]
# for line in contents:
#     current=jieba.lcut(line)
#     for i in range(len(current)):
#         if len(current[i])>1 and current[i]!='\r\n':
#             contents_s.append(current[i])

for line in contents:
    current=jieba.lcut(line)
    if len(current)>1 and current!='\r\n':
            contents_s.append(current)

df_content=pd.DataFrame({'contents_s':contents_s})


stop_words=pd.read_csv(r'stopwords.txt',index_col=False,quoting=3,names=['stop_words'],sep='\t',encoding='utf-8')
#print(stop_words.head())


def drop_stop_words(new_content,new_stopwords):
    contents_clean=[]
    all_words=[]
    for line in new_content:
        line_clean = []
        for i in range(len(line)):
            if line[i] in new_stopwords:
                continue
            else :
                line_clean.append(line[i])
                all_words.append(str(line[i]))
        contents_clean.append(line_clean)
    return contents_clean,all_words

new_content=df_content.contents_s.values.tolist()
new_stopwords=stop_words.stop_words.values.tolist()
contents_clean,all_words=drop_stop_words(new_content,new_stopwords)

print(contents_clean[10])

print(all_words[:10])

df_content=pd.DataFrame({'contents_clean':contents_clean})
df_content.head()
df_all_words=pd.DataFrame({'all_words':all_words})
df_all_words.head()

words_count=df_all_words.groupby(by=['all_words'])['all_words'].agg({"count":numpy.size})
words_count=words_count.reset_index().sort_values(by=["count"],ascending=False)
words_count.head()



from wordcloud import WordCloud
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['figure.figsize'] = (10.0, 5.0)

wordcloud=WordCloud(font_path="./simhei.ttf",background_color="white",max_font_size=80)
word_frequence = {x[0]:x[1] for x in words_count.head(100).values}
wordcloud=wordcloud.fit_words(word_frequence)
plt.imshow(wordcloud)


import jieba.analyse
index = 2400
print (df_news['content'][index])
content_S_str = "".join(contents_s[index])
print ("  ".join(jieba.analyse.extract_tags(content_S_str, topK=5, withWeight=False)))