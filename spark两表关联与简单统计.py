# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(shenxianjun)s

#E_mail: shenxianjun.patrick@gmail.com

"""


#开始spark
import pyspark
from pyspark import SparkContext
from pyspark import SparkConf
from pyspark.sql import SparkSession

conf = SparkConf().setAppName('project1').setMaster('local')
spark= SparkSession.builder.master('local').appName('project1').getOrCreate()
sc = SparkContext.getOrCreate(conf)




#read data
path = r'G:\统计类知识与材料\数据集\movielens_20m_dataset\movie.csv'
schema = None
sep = ','
header = True
movie = spark.read.csv(path = path, schema = schema ,sep = sep, header = header) #读取数据集
print(type(movie)) #查看类型
print(movie)
movie.head(10) #查看前几行 -- 推荐使用
movie.show() #查看资料




#read data
path2 = r'G:\统计类知识与材料\数据集\movielens_20m_dataset\rating.csv'
schema = None
sep = ','
header = True
rating = spark.read.csv(path = path2, schema = schema ,sep = sep, header = header) #读取数据集
print(type(rating)) #查看类型
print(rating)
rating.head(10) #查看前几行 -- 推荐使用
rating.show() #查看资料

movie.count()


rating.count()




from pyspark.sql import functions as F
result1=movie.agg(F.count("movieId"), F.countDistinct("movieId"))
print(result1.show())


#查询是否有重复
from pyspark.sql import functions as F
result2= rating.groupBy(["userId","movieId"]).agg(F.countDistinct("userId").alias("userId_unique_cnt"),F.count("userId").alias("userId_cnt"))
result2.filter((F.col('userId_cnt')>=2)).head()
result2.count()





#数据合并
movie_rating = movie.join(rating, movie.movieId == rating.movieId, how='left')
movie_rating.head()





#每部电影的评论数量

from pyspark.sql import functions as F
result= movie_rating.groupBy(["movieId#1"]).agg(F.countDistinct("userId").alias("comment_cnt")).orderBy('comment_cnt')

result2.count()

movie_rating.head()

movie_rating.columns



movie_rating['genres'].head()




# -*- coding: utf-8 -*-
import pandas as pd
from pyspark.sql import SparkSession
from pyspark.sql import SQLContext
from pyspark import SparkContext

#初始化数据


#spark.DataFrame 转换成 pandas.DataFrame
sqlContest = SQLContext(sc)
df = sqlContest.createDataFrame(movie_rating)

df.head()

print(type(movie_rating)) #查看类型

#显示数据
spark_df.select("c1").show()


# pandas.DataFrame 转换成 spark.DataFrame
pandas_df = sentenceData.toPandas()

#打印数据
print pandas_df




