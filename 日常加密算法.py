# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(shenxianjun)s

#E_mail: shenxianjun.patrick@gmail.com

"""

num=[]
for i in range(0,10):
    num.append(str(i))

num.append(str('你好'))
num.append(str('310104198612143636'))
'''  SHA256 加密  ''''
import hashlib
num_encrypt_256=[]
for i in range(len(num)):
    sha256=hashlib.sha256()
    hash_str=num[i]
    sha256.update(hash_str.encode('utf-8'))
    sha256_values=sha256.hexdigest()
    num_encrypt_256.append(sha256_values)

'''  MD5 加密  ''''
num_encrypt_MD5=[]
for i in range(len(num)):
    md5=hashlib.md5()
    hash_str=num[i]
    md5.update(hash_str.encode('utf-8'))
    md5_values=md5.hexdigest()
    num_encrypt_MD5.append(md5_values)

print(num_encrypt_MD5)


'''  AES 加密  ''''

#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Crypto.Cipher import AES
import base64
PADDING = '\0'
#PADDING = ' '
pad_it = lambda s: s+(16 - len(s)%16)*PADDING
key = '1234567812345678'
iv = '1234567812345678'
source = '你好'
generator = AES.new(key, AES.MODE_CBC, iv)
crypt = generator.encrypt(pad_it(source))
cryptedStr = base64.b64encode(crypt)
print cryptedStr
generator = AES.new(key, AES.MODE_CBC, iv)
recovery = generator.decrypt(crypt)
print recovery.rstrip(PADDING)