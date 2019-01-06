# -*- coding: utf-8 -*-
import pandas as pd

import pandas as pd


#genome_scores=pd.read_csv(r'G:\统计类知识与材料\数据集\movielens_20m_dataset\genome_scores.csv',encoding='utf-8',engine='python')
#genome_tags=pd.read_csv(r'G:\统计类知识与材料\数据集\movielens_20m_dataset\genome_tags.csv',encoding='utf-8',engine='python')
movie=pd.read_csv(r'G:\统计类知识与材料\数据集\movielens_20m_dataset\movie.csv',error_bad_lines=False,engine='python')
rating=pd.read_csv(r'G:\统计类知识与材料\数据集\movielens_20m_dataset\rating.csv',engine='python')
#tag=pd.read_csv(r'G:\统计类知识与材料\数据集\movielens_20m_dataset\tag.csv',encoding='utf-8',error_bad_lines=False, engine='python')

'''
获取最新一笔评论
'''
#result1=rating.groupby(["userId","movieId"])["userId"].unique()

#result2=rating.groupby(["movieId","userId"])["userId"].count()






import time
from sqlalchemy import create_engine

#导入数据

begin=time.clock()
engine = create_engine('postgresql+psycopg2://postgres:sxj168109921@localhost:5432/postgres')
movie.to_sql('movie', engine)
end=time.clock()

print("The function run time is : %.03f seconds" %(end-begin))


begin=time.clock()
engine = create_engine('postgresql+psycopg2://postgres:sxj168109921@localhost:5432/postgres')
rating.to_sql('rating', engine)
end=time.clock()

print("The function run time is : %.03f seconds" %(end-begin))