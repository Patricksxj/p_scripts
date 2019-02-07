import os
os.chdir('D:\P_WORKPLACE')
print(os.getcwd())
from  pyspark.conf import SparkConf
from pyspark.sql import SparkSession
from pyspark import SparkContext
spark =SparkSession.builder.appName("abcd").master("local[4]").getOrCreate()
sc = SparkContext(master="local")
print(spark.version)