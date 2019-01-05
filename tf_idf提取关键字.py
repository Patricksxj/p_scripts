
import jieba
import os
import pandas as pd
import numpy
print(os.chdir('D:\P_WORKPLACE'))
print(os.getcwd())

content_list=[]
#导入文章
with open('./魔道祖师-墨香铜臭.txt','r',encoding='utf-8') as f:
    lines = f.readlines() # 逐行读取
    for line in lines:
        words=line.strip('\n\r\t\s').strip('，：;,。')
        cut_words = jieba.lcut(words)
        if len(cut_words) == 0 or cut_words=='' or cut_words in ('\n','\s','\t','，','：',',',';',',','。','：','：',' '):
            continue
        content_list.append(cut_words)

#print(content_list[:20])


stop_words=pd.read_csv(r'stopwords.txt',index_col=False,quoting=3,names=['stop_words'],sep='\t',encoding='utf-8')



def drop_stop_words(content_list,stop_words):
    contents_clean=[]
    all_words=[]
    for line in content_list:
        line_clean = []
        for i in range(len(line)):
            if line[i] in stop_words:
                continue
            else :
                line_clean.append(line[i])
                all_words.append(str(line[i]))
        contents_clean.append(line_clean)
    return contents_clean,all_words

stop_words=stop_words.stop_words.values.tolist()
contents_clean,all_words=drop_stop_words(content_list,stop_words)

#print(contents_clean[:10])

result=[]
for j in range(len(contents_clean)):
    result=result+contents_clean[j]


import jieba.analyse
analyse_result = "".join(result)
print ("  ".join(jieba.analyse.extract_tags(analyse_result, topK=150, withWeight=False)))


df_all_words=pd.DataFrame({'all_words':all_words})
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
