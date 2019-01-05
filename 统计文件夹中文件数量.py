# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(shenxianjun)s

#E_mail: shenxianjun.patrick@gmail.com

"""

import os
path=r'E:\movie'
aaa=os.listdir(path)




def stat_file(path=r'E:\movie'):
    folder_content=[]
    format_content=[]
    all_file=os.listdir(path)
    for index in range(len(all_file)):
        filename,fileformat=os.path.splitext(path+"\\"+all_file[index])#分离文件名与后缀
        #print(filename,fileformat)
        if fileformat not in ('.mkv','.rmvb','.mp4','.torrent'):
            filename=filename+fileformat
            fileformat=''
        else:
            pass
        if os.path.isdir(filename)==True:#如何发现是文件夹，则进入下一层文件
            string_child=os.listdir(filename)
            for index2 in range(len(string_child)):
                result,child_format=os.path.splitext(string_child[index2])
                folder_content.append(result)
                format_content.append(child_format)
        else:
            result=os.path.basename(filename)
            folder_content.append(result)
            format_content.append(fileformat)

    return folder_content,format_content


folder_content,format_content=stat_file(path=r'G:\movie')




from collections import Counter
a=Counter(format_content)



a=os.path.splitext(r'E:\movie\德云社2016丙申年封箱整场.2017.BD1280高清-www.61vcd.com')

j=0
for i in range(len(folder_content)):
    if format_content[i] in ('.mkv','.rmvb','.mp4'):
        j=j+1
        print(folder_content[i])
print('tatal:',j)
