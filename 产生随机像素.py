# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(shenxianjun)s

#E_mail: shenxianjun.patrick@gmail.com

"""

from PIL import Image
image=Image.open('lena.jpg')
image.show()
image.format

image.size
image.histogram()

len(_)

image.getpixel((100,50))

image.putpixel((100,50),(128,30,120))


from random import randint
im1=Image.open('new_image.bmp')
im1.show()

for w in range(200,280):
    for h in range(100,200):
        r=randint(0,255)
        g=randint(0,255)
        b=randint(0,255)
        im1.putpixel((w,h),(r,g,b))


for w in range(200,280):
    for h in range(100,200):
        color=im1.getpixel((w,h))
        im1.putpixel((w+200,h),color)

im1.show()

im1.save('new1.jpg')