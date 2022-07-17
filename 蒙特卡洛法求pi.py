import numpy as np
import random

def monte_carlo_simiulate(num=10000):
    out_range_cnt=0
    in_range_cnt=0
    for i in range(num):
        x=random.randrange(-100,100)
        y=random.randrange(-100,100)
        if x**2+y**2>100**2:
            out_range_cnt+=1
        else:
            in_range_cnt+=1
    pi=in_range_cnt*4/(out_range_cnt+in_range_cnt)
    return pi
result=monte_carlo_simiulate(num=1000000)
print(result)