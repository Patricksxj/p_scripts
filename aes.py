import base64
import hashlib
from Crypto import Random
from Crypto.Cipher import AES


BS = 16
pad = lambda s:s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
unpad = lambda s:s[:-ord(s[len(s)-1:])]


import base64
from Crypto.Cipher import AES
from Crypto import Random


class AESCipher:
    def __init__(self,key):
        self.key=key
    def encrypt(self,raw):
        raw = pad(raw)
        iv = Random.new().read(AES.block_size)
        cipher=AES.new(self.key,AES.MODE_CFB,iv)
        return base64.b64encode(iv + cipher.encrypt(raw))
    def decrypt(self,enc):
        enc = base64.b64decode(enc)
        iv = enc[:16]
        cipher = AES.new(self.key,AES.MODE_CFB,iv)
        return unpad(cipher.decrypt(enc[16:]))

xxx = AESCipher('1234567812345678')
text = '那么晚了该睡觉了'


text1 = xxx.encrypt(text)
text2 = xxx.decrypt(text1)


def hex2char(data):
#    binascii.a2b_hex(hexstr)
    output = binascii.unhexlify(data)
    print(output)

hex2char(text2)
binascii.a2b_hex(text2)

type(text2‘’.join(["%02x % x for x in bytes"]).strip())


import binascii
print(binascii.unhexlify(b'\xe9\x82\xa3\xe4\xb9\x88\xe6\x99\x9a\xe4\xba\x86\xe8\xaf\xa5\xe7\x9d\xa1\xe8\xa7\x89\xe4\xba\x86'))