import pandas as  pd
import numpy as np
import datetime as dt
df=pd.read_excel('D:\P_WORKPLACE\patrick_shen posts.xlsx',encoding='utf-8')

#df.info()

df['DateTime'] = pd.to_datetime(df['DateTime'])

#df.info()

#print(df['DateTime'])

df2=df[df['DateTime']>pd.to_datetime('2018/01/01', format='%Y/%m/%d')]

#print('df:',df.shape)
#print('df2:',df2.shape)

#判断是否转发
df2['Trans']=df2.Content.apply(lambda x:1 if x[:2] in ('转发','//')   else 0)

#判断是否有GPS

df2['Has_GPS']=df2.Location.apply(lambda x:1 if pd.notnull(x) else 0)

#print(df2['Has_GPS'].head(10))


df2['Has_Pic']=df2.Pic.apply(lambda x:1 if pd.notnull(x) else 0)


df2['Trans_V']=df2.Content.apply(lambda x: x.strip('/').split(':')[0] if x[:2]=='//' else '' )


df2['month']=df2['DateTime'].dt.month

df2['hour']=df2['DateTime'].dt.hour

#df2.to_excel('D:\P_WORKPLACE\新数据.xls')


#df.apply(lambda x: x['Col2'] if x['Col1'].isnull() else x['Col1'], axis=1)

"""
18年发送微博总量
"""
print('18年发送微博总量:',df2['DateTime'].count())
print('18年转发微博量:',df2['Trans'].sum())
print('18年转发占比:{:2.1%}'.format(df2['Trans'].sum()/df2['DateTime'].count()))
print('18年发送微博有定位信息:',df2['Has_GPS'].sum())
#print('18年主要转发人:',df2['Has_GPS'].sum())
#print(df2.groupby(['Trans_V'])['Trans_V'].count())





month_cnt=df2.groupby(['month'])['month'].agg({"count":np.size})
test_df = month_cnt.reset_index()
test_df = test_df.rename(columns={'count':'all_num'}) ##生成数据框
test_df['month_pct']=test_df['all_num']/443






import matplotlib.pyplot as plt
import matplotlib
import matplotlib.ticker as mtick
plt.style.use('ggplot')
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
fig = plt.figure()
ax1=fig.add_subplot(111)
ax2=ax1.twinx()
plt.title('18年各月发送微博数vs发送占比',)
ax1.bar(test_df['month'],test_df['all_num'],color='royalblue')
ax1.set_ylabel(u'发送微博数')
ax1.legend(loc=2)
ax1.grid(False)
#设置右侧Y轴显示百分数
ax2.set_ylim(0,110)
fmt='%.2f%%'
yticks = mtick.FormatStrFormatter(fmt)
ax2.yaxis.set_major_formatter(yticks)
# 绘制成功率图像
ax2.grid(True)
yRightLable=test_df.columns[2]
ax2.plot(test_df['month'],test_df['month_pct']*100,'-.',color='darkorange',label=yRightLable,linewidth=2,marker='.')
ax2.set_xlim([0,13])
ax2.set_ylabel(u'每月发送月报分布')
ax2.set_xlabel(u'月份')
ax2.legend(loc=2)
plt.show()




"""
各小时发送微博情况
"""

hour_cnt=df2.groupby(['hour'])['hour'].agg({"all_num":np.size})
test2_df = hour_cnt.reset_index()
test2_df['hour_pct']=test2_df['all_num']/443


plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
fig = plt.figure()
ax1=fig.add_subplot(111)
ax2=ax1.twinx()
plt.title('18年各小时发送微博数vs发送占比',)
ax1.bar(test2_df['hour'],test2_df['all_num'],color='royalblue')
ax1.set_ylabel(u'发送微博数')
ax1.legend(loc=2)
ax1.grid(False)
#设置右侧Y轴显示百分数
ax2.set_ylim(0,110)
plt.xticks(np.arange(0,26,2))
fmt='%.2f%%'
yticks = mtick.FormatStrFormatter(fmt)
ax2.yaxis.set_major_formatter(yticks)
# 绘制成功率图像
ax2.grid(True)
yRightLable=test2_df.columns[2]
ax2.plot(test2_df['hour'],test2_df['hour_pct']*100,'-.',color='darkorange',label=yRightLable,linewidth=2,marker='.')
ax2.set_xlim(0,25)
ax2.set_ylabel(u'每小时发送月报分布')
ax2.set_xlabel(u'时间')
ax2.legend(loc=2)
plt.show()






words_count=df2.groupby(['Trans_V'])['Trans_V'].agg({"count":np.size})
words_count=words_count.reset_index().sort_values(by=["count"],ascending=False)
print(words_count.head())







from wordcloud import WordCloud
import matplotlib.pyplot as plt
import matplotlib
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['figure.dpi'] = 300 #分辨率
plt.grid(False)
plt.axis('off')
#plt.figure(figsize=(8,4))
plt.tight_layout(pad=0)
wordcloud=WordCloud(font_path="./simhei.ttf",background_color="white",max_font_size=1500,width=1000,height=500)
word_frequence = {x[0]:x[1] for x in words_count.head(100).values}
wordcloud=wordcloud.fit_words(word_frequence)
plt.savefig('wordcloud.png',bbox_inches='tight')
plt.imshow(wordcloud)

