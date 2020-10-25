sent1 = "I love sky, I love sea."
sent2 = "I like running, I love reading."

from nltk import word_tokenize
sents = [sent1, sent2]
texts = [[word for word in word_tokenize(sent)] for sent in sents]
print(texts)

from gensim import corpora
from gensim.similarities import Similarity

#  语料库
dictionary = corpora.Dictionary(texts)

# 利用doc2bow作为词袋模型
corpus = [dictionary.doc2bow(text) for text in texts]

print('corpus:',corpus)

similarity = Similarity('-Similarity-index', corpus, num_features=len(dictionary))
print("similarity：",similarity)
# 获取句子的相似度
new_sensence = sent1
test_corpus_1 = dictionary.doc2bow(word_tokenize(new_sensence))

cosine_sim = similarity[test_corpus_1][1]
print("利用gensim计算得到两个句子的相似度： %.4f。"%cosine_sim)