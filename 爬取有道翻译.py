
"""
有道词典

"""
import urllib.request
import urllib.parse
data={}
data['i']="I love my job"
data['from']='AUTO'
data['to']='AUTO'
data['smartresult']= 'dict'
data['client']= 'fanyideskweb'
data['salt']= '15449337759388'
data['sign']= 'd761d2f5db1454a0022a1b5650fbe7b9'
data['ts']= '1544933775938'
data['bv']= '6f014bd66917f921835d1d6ae8073eb1'
data['doctype']= 'json'
data['version']= '2.1'
data['keyfrom']= 'fanyi.web'
data['action']= 'FY_BY_CLICKBUTTION'
data['typoResult']= 'false'
url=r'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
data=urllib.parse.urlencode(data).encode('utf-8')
response=urllib.request.urlopen(url=url,data=data)
html=response.read().decode('utf-8')
print(html)


import urllib.request
import urllib.parse
head={}
head['user-agent']='Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
url1=r'http://www.ip138.com:8080/search.asp?mobile='
no=r'13524777123'
url2=r'&action=mobile'
url=url1+no+url2
req=urllib.request.Request(r"http://www.ip138.com:8080/search.asp?mobile=13524777123&action=mobile",headers=head)
response=urllib.request.urlopen(req)
html=response.read()
print(html)

import json
#target=json.load(html)