# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(shenxianjun)s

#E_mail: shenxianjun.patrick@gmail.com

"""


file=r'G:\统计类知识与材料\数据集\Tencent_AILab_ChineseEmbedding\Tencent_AILab_ChineseEmbedding.txt'

with open(file,encoding='utf-8') as f:
    for line in f:
        process(line) # <do something with line>

try:
    f = open(r'G:\统计类知识与材料\数据集\Tencent_AILab_ChineseEmbedding\Tencent_AILab_ChineseEmbedding.txt', 'r',encoding='utf-8')
    for line in f.readlines()[0,2]:
        print(line)
finally:
    if f:
        f.close()

for line in f.readlines():
process(line) #


def read_in_chunks(filePath, chunk_size=1024*1024):
    """
    Lazy function (generator) to read a file piece by piece.
    Default chunk size: 1M
    You can set your own chunk size
    """
    file_object = open(filePath,encoding='utf-8')
    while True:
        chunk_data = file_object.read(chunk_size)
        if not chunk_data:
            break
        yield chunk_data


if __name__ == "__main__":
    filePath = r'G:\统计类知识与材料\数据集\Tencent_AILab_ChineseEmbedding\Tencent_AILab_ChineseEmbedding.txt'
    for chunk in read_in_chunks(filePath,chunk_size=10):
        with open(chunk) as f:
            for line in f.readlines()[0,2]:
                print(line)

file=r'G:\统计类知识与材料\数据集\Tencent_AILab_ChineseEmbedding\Tencent_AILab_ChineseEmbedding.txt'


with open(file,"r",encoding='utf-8') as f:
    for line in f.readlines()[0,1]:
        print(line)