import json
from collections import OrderedDict
from gensim.models import KeyedVectors
from annoy import AnnoyIndex

#file='D:\Data_Science\data\Tencent_AILab_ChineseEmbedding\Tencent_AILab_ChineseEmbedding_Min.txt'


#file='D:\Data_Science\data\Tencent_AILab_ChineseEmbedding\Tencent_AILab_ChineseEmbedding.txt'
#tc_wv_model = KeyedVectors.load_word2vec_format(file, binary=False,limit=200000)


#tc_wv_model.save('D:\Data_Science\data\Tencent_AILab_ChineseEmbedding\Tencent_AILab_ChineseEmbedding.bin')
model = KeyedVectors.load('D:\Data_Science\data\Tencent_AILab_ChineseEmbedding\Tencent_AILab_ChineseEmbedding.bin')

print(model.most_similar(positive=['女', '国王'], negative=['男'], topn=1))
print(model.doesnt_match("上海 成都 广州 北京".split(" ")))
print(model.similarity('女人', '男人'))
print(model.most_similar('特朗普', topn=10))
print(model.n_similarity(["中国","北京"],["俄罗斯","莫斯科"]))


print(model.similarity('餐饮', '零售'))
print(model.n_similarity(["卫生","部门"],["零售","风险"]))
print(model.similarity('卫生', '零售'))