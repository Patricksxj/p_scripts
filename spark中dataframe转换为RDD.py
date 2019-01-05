# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(shenxianjun)s

#E_mail: shenxianjun.patrick@gmail.com

"""

#导入的数据转换为RDD

df_rdd = csvDF.rdd.map(lambda x:x).map(list)

df_rdd.collect()

#列的元素展示
result=df_rdd.map(lambda column:column[2]).distinct().collect()

print(result)

df_rdd.collect()


df_rdd_collect = csvDF.rdd.map(lambda x:x).map(list).collect()

df_rdd_collect

#统计每列的数据缺失率
colunms_cnt=len(csvDF.columns)
for i in range(colunms_cnt):
    #获取第i列数据
    columns = [item[i] for item in df_rdd_collect]
    #统计第i列数据中非空的数据数
    count = sum([1 for item in columns if item])
    #计算第i列的数据缺失率
    missing_rate = 1 - count/len(df_rdd_collect)
    print("变量:{} 的数据缺失率为:{:.4f}%".format(csvDF.columns[i],missing_rate*100))




from pyspark.sql import functions as F
df_summary = sorted(csvDF.groupBy(csvDF.1Q).agg(F.max(csvDF.1Q),F.min(csvDF.1Q),F.mean(csvDF.1Q),F.stddev(csvDF.1Q)).collect())


%pyspark

from pyspark.sql import functions as F

#构造原始数据样例
df = spark.createDataFrame([
    (1,175,72,28,'M',10000),
    (2,171,70,45,'M',8000),
    (3,172,None,27,'F',7000),
    (4,180,78,30,'M',4000),
    (5,None,48,54,'F',6000),
    (6,160,45,30,'F',5000),
    (7,169,65,36,'M',7500),],
    ['id','height','weight','age','gender','income'])

#先基于gender分组，然后用各种聚合函数(max,min,mean,stddev)统计age列的信息
df_summary = sorted(df.groupBy(df.gender).agg(F.max(df.age),F.min(df.age),F.mean(df.age),F.stddev(df.age)).collect())

print(df_summary )

csvDF.DATASET[1]

csvDF.collect()

type(df)

type(csvDF)