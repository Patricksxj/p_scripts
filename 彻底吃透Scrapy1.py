

import urllib.request
'''
Request对象
'''
request_result=urllib.request.Request("http://placekitten.com/1024/768")
html=urllib.request.urlopen(request_result)
contents=html.read()
print(contents)


with open(r'D:\P_WORKPLACE\cat_image.jpg','wb') as f:
    f.write(contents)


'''
方法2：url地址
'''


import urllib.request
request_result2=urllib.request.urlopen("http://placekitten.com/1024/768")
contents2=request_result2.read()
print(contents2)
print(request_result2.geturl())
print(request_result2.info())
print(request_result2.getcode())


with open(r'D:\P_WORKPLACE\cat_image2.jpg','wb') as f:
    f.write(contents2)

