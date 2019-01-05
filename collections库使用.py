# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(shenxianjun)s

#E_mail: shenxianjun.patrick@gmail.com

"""

from collections import Counter

result=Counter("asdsadasdasdasdasdasdasdvfvfffedfefefe")

result2=result.keys()

result.items()


type(result2)

c=Counter('nihao')

c.update('shentibushufu')

c.subtract('shentibushufu')

del c.keys(list(c.keys()==0))


"""
返回一个迭代器。元素被重复了多少次，在该迭代器中就包含多少个该元素。
元素排列无确定顺序，个数小于1的元素不被包含。
"""
new=list(c.elements())


"""
返回一个TopN列表。如果n没有被指定，则返回所有元素。

当多个元素计数值相同时，排列是无确定顺序的。

"""

c.most_common(3)


foo1=1.0

foo2=1.0

id(foo1)
id(foo2)


"""
浅copy
"""

result_a=Counter(a=4,b=5,c=6)

result_b=result_a.copy()

result_a

result_b


result_b.update('bbb')


result_b

a=['1']

b=a[:]

c=list(b)

c=b.copy()

b='2'

a,b,c




c = Counter("abcdcba")

d = c.copy()

c,d


d.subtract('a')




c.most_common()[:-3:-1]



"""

deque用法

"""

import sys
import time
from collections import deque

fancy_loading = deque('>--------------------')

while True:
    print ('\r%s' % ''.join(fancy_loading))
    fancy_loading.rotate(1)
    sys.stdout.flush()
    time.sleep(0.08)




a=(('a',1),('c',3),('b',2))

b=dict(a)

from collections import OrderedDict

d=OrderedDict(a)

for v,k in b.items():
    print("v=%s,k=%s" %(v,k))



for v,k in d.items():
    print("v=%s,k=%s" %(v,k))




items = (
    ('A', 1),
    ('B', 2),
    ('C', 3)
)

regular_dict = dict(items)
ordered_dict = OrderedDict(items)

print ('Regular Dict:')
for k, v in regular_dict.items():
    print (k, v)

print ('Ordered Dict:')
for k, v in ordered_dict.items():
    print (k, v)




