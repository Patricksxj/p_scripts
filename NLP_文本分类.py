
# coding: utf-8

# In[73]:


import random
import jieba
import pandas as pd
import os
import jieba.analyse
from sklearn import metrics


# In[3]:


os.getcwd()
os.chdir(r'D:\P_WORKPLACE')


# In[26]:


# 加载停用词
stopwords = pd.read_csv('stop_words.txt', index_col=False, quoting=3, sep="\t", names=['stopword'],encoding='gbk')


# In[9]:


stopwords.head()


# In[27]:


stopwords = stopwords['stopword'].values


# In[41]:



# 加载语料
laogong_df = pd.read_csv('beilaogongda.csv', encoding='utf-8', sep=',')
laopo_df = pd.read_csv('beilaogongda.csv', encoding='utf-8', sep=',')
erzi_df = pd.read_csv('beierzida.csv', encoding='utf-8', sep=',')
nver_df = pd.read_csv('beinverda.csv', encoding='utf-8', sep=',')
# 删除语料的nan行
laogong_df.dropna(inplace=True)
laopo_df.dropna(inplace=True)
erzi_df.dropna(inplace=True)
nver_df.dropna(inplace=True)
# 转换
laogong = laogong_df.segment.values.tolist()
laopo = laopo_df.segment.values.tolist()
erzi = erzi_df.segment.values.tolist()
nver = nver_df.segment.values.tolist()


# In[42]:


jieba.suggest_freq('报警人', True)


# In[43]:


# 定义分词和打标签函数preprocess_text
# 参数content_lines即为上面转换的list
# 参数sentences是定义的空list，用来储存打标签之后的数据
# 参数category 是类型标签
def preprocess_text(content_lines, sentences, category):
    for line in content_lines:
        try:
            segs = jieba.lcut(line)
            segs = [v for v in segs if not str(v).isdigit()]  # 去数字
            segs = list(filter(lambda x: x.strip(), segs))  # 去左右空格
            segs = list(filter(lambda x: len(x) > 1, segs))  # 长度为1的字符
            segs = list(filter(lambda x: x not in stopwords, segs))  # 去掉停用词
            sentences.append((" ".join(segs), category))  # 打标签
        except Exception:
            print(line)
            continue


sentences = []
preprocess_text(laogong, sentences,0)
preprocess_text(laopo, sentences, 1)
preprocess_text(erzi, sentences, 2)
preprocess_text(nver, sentences, 3)


# In[37]:



len(sentences)


# In[44]:


sentences[:10]


# In[46]:


random.shuffle(sentences)


# In[47]:


sentences[:10]


# In[67]:


for sentence in sentences[:10]:
    print(sentence[0], sentence[1])  # 下标0是词列表，1是标签


# In[107]:


#用词袋建模
from sklearn.feature_extraction.text import CountVectorizer
vec = CountVectorizer(analyzer='word', # tokenise by character ngrams
        max_features=4000)

#拆分训练集与测试集
from sklearn.model_selection import train_test_split
x, y = zip(*sentences)
#type(sentences)

x_train, x_test, y_train, y_test = train_test_split(x,y, random_state=1256)

vec.fit(x_train)


# In[108]:


from sklearn.naive_bayes import MultinomialNB
classifier = MultinomialNB()
classifier.fit(vec.transform(x_train), y_train)
pre = classifier.predict(vec.transform(x_test))


# In[81]:


type(list(pre))


# In[79]:


type(y_test)


# In[109]:


print("Naive_Bayes_Accuracy : %.4g" % metrics.accuracy_score(y_test,pre))


# In[101]:



print(classifier.score(vec.transform(x_test), y_test))


# In[110]:


from sklearn.svm import SVC
svm = SVC(kernel='linear')
svm.fit(vec.transform(x_train), y_train)
print(svm.score(vec.transform(x_test), y_test))


# In[103]:


from sklearn.ensemble import GradientBoostingClassifier
gbm0 = GradientBoostingClassifier(random_state=10)
gbm0.fit(vec.transform(x_train), y_train)
y_pred = gbm0.predict(vec.transform(x_test))
print("GBDT_Accuracy : %.4g" % metrics.accuracy_score(y_test,list(y_pred)))


# In[87]:


params = {
        'booster': 'gbtree',     #使用gbtree
        'objective': 'multi:softmax',  # 多分类的问题、
        # 'objective': 'multi:softprob',   # 多分类概率
        #'objective': 'binary:logistic',  #二分类
        'eval_metric': 'merror',   #logloss
        'num_class': 4,  # 类别数，与 multisoftmax 并用
        'gamma': 0.1,  # 用于控制是否后剪枝的参数,越大越保守，一般0.1、0.2这样子。
        'max_depth': 8,  # 构建树的深度，越大越容易过拟合
        'alpha': 0,   # L1正则化系数
        'lambda': 10,  # 控制模型复杂度的权重值的L2正则化项参数，参数越大，模型越不容易过拟合。
        'subsample': 0.7,  # 随机采样训练样本
        'colsample_bytree': 0.5,  # 生成树时进行的列采样
        'min_child_weight': 3,
        # 这个参数默认是 1，是每个叶子里面 h 的和至少是多少，对正负样本不均衡时的 0-1 分类而言
        # 假设 h 在 0.01 附近，min_child_weight 为 1 叶子节点中最少需要包含 100 个样本。
        'silent': 0,  # 设置成1则没有运行信息输出，最好是设置为0.
        'eta': 0.03,  # 如同学习率
        'seed': 1000,
        'nthread': -1,  # cpu 线程数
        'missing': 1
    }


# In[88]:


import xgboost as xgb
from sklearn.model_selection import StratifiedKFold
import numpy as np

# xgb矩阵赋值
xgb_train = xgb.DMatrix(vec.transform(x_train), label=y_train)
xgb_test = xgb.DMatrix(vec.transform(x_test))


# In[89]:


model = xgb.train(dtrain=xgb_train, params=params,num_boost_round=500)


# In[90]:


ypred = model.predict(xgb_test)


# In[92]:


print("xgboost_Accuracy : %.4g" % metrics.accuracy_score(y_test,list(ypred)))

