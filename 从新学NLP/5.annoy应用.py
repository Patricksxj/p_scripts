import json
from collections import OrderedDict
from gensim.models import KeyedVectors
from annoy import AnnoyIndex

#首次读取
'''
file='D:\Data_Science\data\Tencent_AILab_ChineseEmbedding\Tencent_AILab_ChineseEmbedding.txt'
tc_wv_model = KeyedVectors.load_word2vec_format(file, binary=False,limit=200000)


# 把txt文件里的词和对应的向量，放入有序字典
word_index = OrderedDict()
for counter, key in enumerate(tc_wv_model.vocab.keys()):
    word_index[key] = counter

# 本地保存
with open(r'D:\Data_Science\data\Tencent_AILab_ChineseEmbedding\tc_word_index.json', 'w') as fp:
    json.dump(word_index, fp)

# 腾讯词向量是两百维的
tc_index = AnnoyIndex(200,metric='angular')
i = 0
for key in tc_wv_model.vocab.keys():
    v = tc_wv_model[key]
    tc_index.add_item(i, v)
    i += 1

tc_index.build(10)

# 将这份index存到硬盘
tc_index.save(r'D:\Data_Science\data\Tencent_AILab_ChineseEmbedding\tc_index_build10.index')
'''

#后续读取
with open(r'D:\Data_Science\data\Tencent_AILab_ChineseEmbedding\tc_word_index.json', 'r') as fp:
    word_index = json.load(fp)

tc_index = AnnoyIndex(200,metric='angular')
tc_index.build(10)
tc_index.load (r'D:\Data_Science\data\Tencent_AILab_ChineseEmbedding\tc_index_build10.index')



# 反向id==>word映射词表
reverse_word_index = dict([(value, key) for (key, value) in word_index.items()])

# get_nns_by_item基于annoy查询词最近的10个向量，返回结果是个list，里面元素是索引
for item in tc_index.get_nns_by_item(word_index[u'卖空'], 10):
    print(reverse_word_index[item])  # 用每个索引查询word

print(tc_index.get_distance(word_index['卫生'],word_index['风险'])) #计算的值是平方距离
#https://github.com/spotify/annoy