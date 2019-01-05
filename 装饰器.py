# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(shenxianjun)s

#E_mail: shenxianjun.patrick@gmail.com

"""

import time

def decorator(func):
    def wrapper(*args, **kwargs):
        t = time.time()
        ans = func(*args, **kwargs)
        t = time.time() - t
        return ans, t
    return wrapper

@decorator
def func():
    for _ in range(10 ** 6):
        x = 0
    return "Done"

func()


import time
import wrapt

def decorator(eps):
    @wrapt.decorator
    def wrapper(func, instance, args, kwargs):
        t = time.time()
        ans = func(*args, **kwargs)
        t = time.time() - t
        if t > eps: print("Slow!")
        else: print("Fast!")
        return ans, t
    return wrapper


@decorator(0.01)
def func1():
    for _ in range(10 ** 6):
        x = 0
    return "Done"

func1()


@decorator(0.05)
def func2():
    for _ in range(10 ** 6):
        x = 0
    return "Done"

func2()