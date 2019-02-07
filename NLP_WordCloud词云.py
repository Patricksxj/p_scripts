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

jieba.load_userdict("./person.txt")
#result=jieba.lcut('何小嫚你好呀')
#print(result)
STOP_WORDS = set([w.strip() for w in open("./stopwords.txt",encoding='utf-8').readlines()])
print(STOP_WORDS)

"""

class MyChapters(object):
    def __init__(self, chapter_list):
        self.chapter_list = chapter_list

    def __iter__(self):
        for chapter in self.chapter_list:
            yield cut_words_with_pos(chapter)


def split_by_chapter(filepath):
    text = open(filepath).read()
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


def grey_color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    return choice(["rgb(94,38,18)", "rgb(128,128,105)", "rgb(39,72,98)"])
"""

def draw_cloud(mask_path, word_freq, save_path):
    mask = imread(mask_path)
    wc = WordCloud(font_path='./kaiti.TTF',  # 设置字体
                   background_color="black",  # 背景颜色
                   max_words=500,  # 词云显示的最大词数
                   mask=mask,  # 设置背景图片
                   max_font_size=80,  # 字体最大值
                   # random_state=42,
                   )
    wc.generate_from_frequencies(word_freq)

    # show
    image_colors = ImageColorGenerator(mask)
    plt.figure()
    plt.imshow(wc.recolor(color_func=image_colors), interpolation='bilinear')
    plt.axis("off")
    wc.to_file(save_path)
    plt.show()
    return


if __name__ == '__main__':
    # freq = person_word("刘峰")
    # input_freq = freq.to_dict()

    freq = pd.read_csv("./cnthe.csv", header=None, index_col=0)
    input_freq = freq[1].to_dict()
    draw_cloud("./he.png", input_freq, "./hexiaoman.png")