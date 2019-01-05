# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(shenxianjun)s

#E_mail: shenxianjun.patrick@gmail.com

"""

"""

输出“水仙花数” 。 所谓水仙花数是指1个3位的十进制数， 其各位数
字的立方和等于该数本身。 例如： 153是水仙花数， 因为153 = 13 + 53 + 33

"""

for i in range(100,1000):
    bai=i//100
    shi=i//10%10
    ge=i%10
    if bai**3+shi**3+ge**3==i:
        print("i=%d" ,i)



    151//10

    891//10%10

