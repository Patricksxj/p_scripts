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
conf = SparkConf().setAppName('project1').setMaster('local[4]')
from pyspark.sql import SparkSession
spark= SparkSession.builder.master('local').appName('project1').getOrCreate()
sc = SparkContext.getOrCreate(conf)




from pyspark.sql import SparkSession

#使用builder模式创建SparkSession
spark = SparkSession.builder\
    .master("local")\
    .appName("project1")\
    .enableHiveSupport()\
    .getOrCreate()

#create rdd
data = sc.parallelize([('amber',22),('alfred',23),('skye',4),('albert',12),('amber',9)])

data.glom().collect()


#.collect（）方法将RDD的所有元素返回到驱动程序，并将其作为列表序列化。

data_heterogenous = sc.parallelize([('Ferrari','fast'),{'Porsche':100000},['Spain','visited',4504]]).collect()



data_heterogenous[1]


data

#建立一个rdd
wordsList = ['cat','elephant','rat','cat','rabbit','elephant','donkey']
wordsRDD = sc.parallelize(wordsList,2)#parallelize
print(type(wordsRDD))                    #查看类型
wordsRDD.count()                         #查看行数
wordsRDD.take(5)                         #前5个项目
wordsRDD.collect()                       #适用于小数据量


#read data
path = r'D:/P_WORKPLACE/nba_data.csv'
schema = None
sep = ','
header = True
csvDF = spark.read.csv(path = path, schema = schema ,sep = sep, header = header) #读取数据集
print(type(csvDF)) #查看类型
print(csvDF)
csvDF.head() #查看前几行 -- 推荐使用
csvDF.show() #查看资料



## 读取txt
textDF = spark.read.text(paths = path)
textDF.head() #查看前几行 -- 推荐使用
textDF.show() #查看资料

## 读取json文件
jsonDF = spark.read.json('hdfs://tmp/json_example.json')
jsonDF.head() #查看前几行 -- 推荐使用
jsonDF.show() #查看资料



print(csvDF.columns[1])
type(csvDF)
csvDF.count()

distinct_teams=csvDF.map(lambda teams:teams).distinct().collect()

distinct_gender = data_from_file_conv.map(lambda row: row[5]).distinct().collect()
distinct_gender


csvDF.show()

csvDF.printSchema()
csvDf.columns

csvDF[2,2]
%pyspark

#生成一段JSON数据
stringJSONRDD = sc.parallelize(("""
  {"id":"123",
"name":"Katie",
"age":19,
"eyeColor":"brown"
  }""",
"""{
"id":"456",
"name":"Michael",
"age":21,
"eyeColor":"blue"
  }""",
"""{
"id":"789",
"name":"Jack",
"age":23,
"eyeColor":"Black"
  }"""))

#创建一个DataFrame
swimmersJSON = spark.read.json(stringJSONRDD)

#1.输出DataFrame中的元素
print("1.输出DataFrame中的元素:\n")
swimmersJSON.show()

#2.输出DataFrame的Schema模式（名称和类型）
print("2.输出DataFrame的Schema模式（名称和类型）:\n")
swimmersJSON.printSchema()

type(swimmersJSON)



#spark sql
"""
创建一个临时视图
"""

csvDF.createOrReplaceTempView("csvDF")
spark.sql("select  DATASET ,DATE , TEAMS from csvDF where TEAMS='Boston'").show()

