# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(shenxianjun)s

#E_mail: shenxianjun.patrick@gmail.com

"""

import json
import pandas as pd

result1=[]
result2=[]
i=0
df_temp=pd.DataFrame({})
with open("json_test.txt",'r') as f:
    for line in f:
        if 'var' in line.strip().split('\t')[0]:
            pass
        else:
            var1,var2,var3=line.strip().split('\t')[:3]
            print('var1:%s,var2:%s,var3:%s' %(var1,var2,var3))
            i=i=1
            temp=json.loads(var3)
            df_data_temp1=pd.DataFrame({'var1':var1,'var2':var2},index=[i])
            df_data_temp2=pd.DataFrame(temp,index=[i])
            df_data_temp=pd.concat([df_data_temp1,df_data_temp2],axis=1)
            df_temp=df_temp.append(df_data_temp,ignore_index=True)
    f.close()
