# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(shenxianjun)s

#E_mail: shenxianjun.patrick@gmail.com

"""

import time
from sqlalchemy import create_engine
import pandas as pd

engine= create_engine('postgresql+psycopg2://postgres:sxj168109921@localhost:5432/postgres')




begin=time.clock()
del df
i=0
j=0
df=pd.DataFrame(columns=('name','num1','num2','num3','num4','num5','num6','num7','num8','num9','num10','num11','num12','num13','num14','num15','num16','num17','num18','num19','num20','num21','num22','num23','num24','num25','num26','num27','num28','num29','num30','num31','num32','num33','num34','num35','num36','num37','num38','num39','num40','num41','num42','num43','num44','num45','num46','num47','num48','num49','num50','num51','num52','num53','num54','num55','num56','num57','num58','num59','num60','num61','num62','num63','num64','num65','num66','num67','num68','num69','num70','num71','num72','num73','num74','num75','num76','num77','num78','num79','num80','num81','num82','num83','num84','num85','num86','num87','num88','num89','num90','num91','num92','num93','num94','num95','num96','num97','num98','num99','num100','num101','num102','num103','num104','num105','num106','num107','num108','num109','num110','num111','num112','num113','num114','num115','num116','num117','num118','num119','num120','num121','num122','num123','num124','num125','num126','num127','num128','num129','num130','num131','num132','num133','num134','num135','num136','num137','num138','num139','num140','num141','num142','num143','num144','num145','num146','num147','num148','num149','num150','num151','num152','num153','num154','num155','num156','num157','num158','num159','num160','num161','num162','num163','num164','num165','num166','num167','num168','num169','num170','num171','num172','num173','num174','num175','num176','num177','num178','num179','num180','num181','num182','num183','num184','num185','num186','num187','num188','num189','num190','num191','num192','num193','num194','num195','num196','num197','num198','num199','num200'))
with open(r'G:\统计类知识与材料\数据集\Tencent_AILab_ChineseEmbedding\Tencent_AILab_ChineseEmbedding.txt', 'r', encoding = 'utf-8') as f:
    while True:
        line = f.readline()  # 逐行读取
        if i==0 :
            pass
        else:
            data=pd.DataFrame(line.strip('\n').split(' '),columns=[j],index=['name','num1','num2','num3','num4','num5','num6','num7','num8','num9','num10','num11','num12','num13','num14','num15','num16','num17','num18','num19','num20','num21','num22','num23','num24','num25','num26','num27','num28','num29','num30','num31','num32','num33','num34','num35','num36','num37','num38','num39','num40','num41','num42','num43','num44','num45','num46','num47','num48','num49','num50','num51','num52','num53','num54','num55','num56','num57','num58','num59','num60','num61','num62','num63','num64','num65','num66','num67','num68','num69','num70','num71','num72','num73','num74','num75','num76','num77','num78','num79','num80','num81','num82','num83','num84','num85','num86','num87','num88','num89','num90','num91','num92','num93','num94','num95','num96','num97','num98','num99','num100','num101','num102','num103','num104','num105','num106','num107','num108','num109','num110','num111','num112','num113','num114','num115','num116','num117','num118','num119','num120','num121','num122','num123','num124','num125','num126','num127','num128','num129','num130','num131','num132','num133','num134','num135','num136','num137','num138','num139','num140','num141','num142','num143','num144','num145','num146','num147','num148','num149','num150','num151','num152','num153','num154','num155','num156','num157','num158','num159','num160','num161','num162','num163','num164','num165','num166','num167','num168','num169','num170','num171','num172','num173','num174','num175','num176','num177','num178','num179','num180','num181','num182','num183','num184','num185','num186','num187','num188','num189','num190','num191','num192','num193','num194','num195','num196','num197','num198','num199','num200']).T
            df=df.append(data)
#            print(df.loc[j])
        j=j+1
        i=i+1
#        print(i)
        if j%1000==0:
            df.to_sql('tencent_nlp_corp', engine, if_exists='append', index=False,chunksize=1000)
            del df
            df=pd.DataFrame(columns=('name','num1','num2','num3','num4','num5','num6','num7','num8','num9','num10','num11','num12','num13','num14','num15','num16','num17','num18','num19','num20','num21','num22','num23','num24','num25','num26','num27','num28','num29','num30','num31','num32','num33','num34','num35','num36','num37','num38','num39','num40','num41','num42','num43','num44','num45','num46','num47','num48','num49','num50','num51','num52','num53','num54','num55','num56','num57','num58','num59','num60','num61','num62','num63','num64','num65','num66','num67','num68','num69','num70','num71','num72','num73','num74','num75','num76','num77','num78','num79','num80','num81','num82','num83','num84','num85','num86','num87','num88','num89','num90','num91','num92','num93','num94','num95','num96','num97','num98','num99','num100','num101','num102','num103','num104','num105','num106','num107','num108','num109','num110','num111','num112','num113','num114','num115','num116','num117','num118','num119','num120','num121','num122','num123','num124','num125','num126','num127','num128','num129','num130','num131','num132','num133','num134','num135','num136','num137','num138','num139','num140','num141','num142','num143','num144','num145','num146','num147','num148','num149','num150','num151','num152','num153','num154','num155','num156','num157','num158','num159','num160','num161','num162','num163','num164','num165','num166','num167','num168','num169','num170','num171','num172','num173','num174','num175','num176','num177','num178','num179','num180','num181','num182','num183','num184','num185','num186','num187','num188','num189','num190','num191','num192','num193','num194','num195','num196','num197','num198','num199','num200'))
        else:
            pass
    df.to_sql('tencent_nlp_corp', engine, if_exists='append', index=False,chunksize=1000)
end=time.clock()
print("The function run time is : %.03f seconds" %(end-begin))


#The function run time is : 49.639 seconds


def write_to_table(df, table_name, if_exists='fail'):
    import io
    import pandas as pd
    from sqlalchemy import create_engine
    db_engine = create_engine('postgresql+psycopg2://postgres:sxj168109921@localhost:5432/postgres')# 初始化引擎
    string_data_io = io.StringIO()
    df.to_csv(string_data_io, sep='|', index=False)
    pd_sql_engine = pd.io.sql.pandasSQL_builder(db_engine)
    table = pd.io.sql.SQLTable(table_name, pd_sql_engine, frame=df,
                               index=False, if_exists=if_exists,schema = 'public')
    table.create()
    string_data_io.seek(0)
    string_data_io.readline()  # remove header
    with db_engine.connect() as connection:
        with connection.connection.cursor() as cursor:
            copy_cmd = "COPY public.%s FROM STDIN HEADER DELIMITER '|' CSV" %table_name
            cursor.copy_expert(copy_cmd, string_data_io)
        connection.connection.commit()


'''
方法2
'''

begin=time.clock()
del df
i=0
j=0
df=pd.DataFrame(columns=('name','num1','num2','num3','num4','num5','num6','num7','num8','num9','num10','num11','num12','num13','num14','num15','num16','num17','num18','num19','num20','num21','num22','num23','num24','num25','num26','num27','num28','num29','num30','num31','num32','num33','num34','num35','num36','num37','num38','num39','num40','num41','num42','num43','num44','num45','num46','num47','num48','num49','num50','num51','num52','num53','num54','num55','num56','num57','num58','num59','num60','num61','num62','num63','num64','num65','num66','num67','num68','num69','num70','num71','num72','num73','num74','num75','num76','num77','num78','num79','num80','num81','num82','num83','num84','num85','num86','num87','num88','num89','num90','num91','num92','num93','num94','num95','num96','num97','num98','num99','num100','num101','num102','num103','num104','num105','num106','num107','num108','num109','num110','num111','num112','num113','num114','num115','num116','num117','num118','num119','num120','num121','num122','num123','num124','num125','num126','num127','num128','num129','num130','num131','num132','num133','num134','num135','num136','num137','num138','num139','num140','num141','num142','num143','num144','num145','num146','num147','num148','num149','num150','num151','num152','num153','num154','num155','num156','num157','num158','num159','num160','num161','num162','num163','num164','num165','num166','num167','num168','num169','num170','num171','num172','num173','num174','num175','num176','num177','num178','num179','num180','num181','num182','num183','num184','num185','num186','num187','num188','num189','num190','num191','num192','num193','num194','num195','num196','num197','num198','num199','num200'))
with open(r'G:\统计类知识与材料\数据集\Tencent_AILab_ChineseEmbedding\Tencent_AILab_ChineseEmbedding.txt', 'r', encoding = 'utf-8') as f:
    while i<=10000:
        line = f.readline()  # 逐行读取
        if i==0 :
            pass
        else:
            data=pd.DataFrame(line.strip('\n').split(' '),columns=[j],index=['name','num1','num2','num3','num4','num5','num6','num7','num8','num9','num10','num11','num12','num13','num14','num15','num16','num17','num18','num19','num20','num21','num22','num23','num24','num25','num26','num27','num28','num29','num30','num31','num32','num33','num34','num35','num36','num37','num38','num39','num40','num41','num42','num43','num44','num45','num46','num47','num48','num49','num50','num51','num52','num53','num54','num55','num56','num57','num58','num59','num60','num61','num62','num63','num64','num65','num66','num67','num68','num69','num70','num71','num72','num73','num74','num75','num76','num77','num78','num79','num80','num81','num82','num83','num84','num85','num86','num87','num88','num89','num90','num91','num92','num93','num94','num95','num96','num97','num98','num99','num100','num101','num102','num103','num104','num105','num106','num107','num108','num109','num110','num111','num112','num113','num114','num115','num116','num117','num118','num119','num120','num121','num122','num123','num124','num125','num126','num127','num128','num129','num130','num131','num132','num133','num134','num135','num136','num137','num138','num139','num140','num141','num142','num143','num144','num145','num146','num147','num148','num149','num150','num151','num152','num153','num154','num155','num156','num157','num158','num159','num160','num161','num162','num163','num164','num165','num166','num167','num168','num169','num170','num171','num172','num173','num174','num175','num176','num177','num178','num179','num180','num181','num182','num183','num184','num185','num186','num187','num188','num189','num190','num191','num192','num193','num194','num195','num196','num197','num198','num199','num200']).T
            write_to_table(data, 'tencent_nlp_corp', if_exists='append')
#            print(df.loc[j])
        i=i+1
#        print(i)
end=time.clock()
print("The function run time is : %.03f seconds" %(end-begin))

