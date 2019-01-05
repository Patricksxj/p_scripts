# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(shenxianjun)s

#E_mail: shenxianjun.patrick@gmail.com

"""




import pandas as pd

country1 = pd.Series({'Name': '中国',
                    'Language': 'Chinese',
                    'Area': '9.597M km2',
                     'Happiness Rank': 79})

country2 = pd.Series({'Name': '美国',
                    'Language': 'English (US)',
                    'Area': '9.834M km2',
                     'Happiness Rank': 14})

country3 = pd.Series({'Name': '澳大利亚',
                    'Language': 'English (AU)',
                    'Area': '7.692M km2',
                     'Happiness Rank': 9})

df = pd.DataFrame([country1, country2, country3], index=['CH', 'US', 'AU'])


df.drop(['Name'],axis=1)

print()