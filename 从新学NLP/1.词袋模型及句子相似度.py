from nltk import word_tokenize
#import nltk
#nltk.download('punkt')
sent1 = "I love sky, I love sea."
sent2 = "I like running, I love reading."
sents = [sent1, sent2]
print("sents:",sents)
##拆词
texts = [[word for word in word_tokenize(sent)] for sent in sents]
print("texts:",texts)
all_list = []
for text in texts:
    all_list += text
corpus = set(all_list)
print(corpus)


#语料做映射
corpus_dict = dict(zip(corpus, range(len(corpus))))
print(corpus_dict)


# 建立句子的向量表示
def vector_rep(text, corpus_dict):
    vec = []
    for key in corpus_dict.keys():
        if key in text:
            vec.append((corpus_dict[key], text.count(key)))
        else:
            vec.append((corpus_dict[key], 0))

    vec = sorted(vec, key= lambda x: x[0])

    return vec

vec1 = vector_rep(texts[0], corpus_dict)
vec2 = vector_rep(texts[1], corpus_dict)
print("vec1:",vec1)
print("vec1:",vec1[1])

#开始计算相似度

from math import sqrt
def similarity_with_2_sents(vec1, vec2):
    inner_product = 0
    square_length_vec1 = 0
    square_length_vec2 = 0
    for tup1, tup2 in zip(vec1, vec2):
        inner_product += tup1[1]*tup2[1]
        square_length_vec1 += tup1[1]**2
        square_length_vec2 += tup2[1]**2

    return (inner_product/sqrt(square_length_vec1*square_length_vec2))


cosine_sim = similarity_with_2_sents(vec1, vec2)
print('两个句子的余弦相似度为： %.4f。'%cosine_sim)






