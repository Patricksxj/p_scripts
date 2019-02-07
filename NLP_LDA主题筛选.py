import os

os.chdir(r'G:\统计类知识与材料\NLP\LDA主题模型案例\novel_analysis-master\data')
#print(os.getcwd())


import jieba
import jieba.posseg
import re
#from basic import *
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
from scipy.misc import imread
from random import choice
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
import lda
import matplotlib.pyplot as plt
import seaborn as sns

jieba.load_userdict("./person.txt")
#result=jieba.lcut('何小嫚你好呀')
#print(result)
STOP_WORDS = set([w.strip() for w in open("./stopwords.txt",encoding='utf-8').readlines()])
print(STOP_WORDS)



class MyChapters(object):
    def __init__(self, chapter_list):
        self.chapter_list = chapter_list

    def __iter__(self):
        for chapter in self.chapter_list:
            yield cut_words_with_pos(chapter)


def split_by_chapter(filepath):
    text = open(filepath,encoding='utf-8').read()
    chapter_list = re.split(r'第.{1,3}章\n', text)[1:]
    return chapter_list


def cut_words_with_pos(text):
    seg = jieba.posseg.cut(text)
    res = []
    for i in seg:
        if i.flag in ["a", "v", "x", "n", "an", "vn", "nz", "nt", "nr"] and is_fine_word(i.word):
            res.append(i.word)

    return list(res)


# 过滤词长，过滤停用词，只保留中文
def is_fine_word(word, min_length=2):
    rule = re.compile(r"^[\u4e00-\u9fa5]+$")
    if len(word) >= min_length and word not in STOP_WORDS and re.search(rule, word):
        return True
    else:
        return False



def person_word(name):
    lines = open("./芳华-严歌苓.txt", "r",encoding='utf-8').readlines()
    word_list = []
    for line in lines:
        if name in line:
            words = cut_words_with_pos(line)
            word_list += words

    cnt = pd.Series(word_list).value_counts()

    return cnt



def get_lda_input(chapters):
    corpus = [" ".join(word_list) for word_list in chapters]
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(corpus)
    return X.toarray(), vectorizer


def lda_train(weight, vectorizer):
    model = lda.LDA(n_topics=20, n_iter=1000, random_state=1)
    model.fit(weight)

    doc_num = len(weight)
    topic_word = model.topic_word_
    vocab = vectorizer.get_feature_names()
    titles = ["第{}章".format(i) for i in range(1, doc_num + 1)]

    n_top_words = 20
    for i, topic_dist in enumerate(topic_word):
        topic_words = np.array(vocab)[np.argsort(topic_dist)][:-(n_top_words + 1):-1]
        print('Topic {}: {}'.format(i, ' '.join(topic_words)))

    doc_topic = model.doc_topic_
    print(doc_topic, type(doc_topic))
    plot_topic(doc_topic)
    for i in range(doc_num):
        print("{} (top topic: {})".format(titles[i], np.argsort(doc_topic[i])[:-4:-1]))


def main():
    chapter_list = split_by_chapter("./芳华-严歌苓.txt")
    chapters = MyChapters(chapter_list)
    weight, vectorizer = get_lda_input(chapters)
    lda_train(weight, vectorizer)


def plot_topic(doc_topic):
    f, ax = plt.subplots(figsize=(10, 4))
    cmap = sns.cubehelix_palette(start=1, rot=3, gamma=0.8, as_cmap=True)
    sns.heatmap(doc_topic, cmap=cmap, linewidths=0.05, ax=ax)
    ax.set_title('proportion per topic in every chapter')
    ax.set_xlabel('topic')
    ax.set_ylabel('chapter')
    plt.show()

    f.savefig('./topic_heatmap.jpg', bbox_inches='tight')


if __name__ == '__main__':
    main()
