# -*- coding: utf-8 -*-
#coding=utf-8
from base64 import b64decode
from Crypto.Cipher import AES
import base64
from hashlib import sha256
import hmac


# Padding for the input string --not
# related to encryption itself.
BLOCK_SIZE = 16  # Bytes
# pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * \
#                 chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)
unpad = lambda s: s[:-ord(s[len(s) - 1:])]

def pad(s ):
    trueLength = s.encode("utf-8")
    leftLength =  BLOCK_SIZE - len(trueLength) % BLOCK_SIZE
    return s + leftLength *chr(leftLength)

#https://www.freesion.com/article/4652397300/
#加密aes/ecb/padding5
def AesECBEncrypt(data,keySecret):
    #对应golang里面
    #data 跟keySecert都是string
    #使用.encode('utf-8')进行编码 相当于[]byte(data)转化成字节数组
    raw = pad(data)
    #通过key值，使用ECB模式进行加密
    cipher = AES.new(keySecret.encode('utf-8'), AES.MODE_ECB)
        #返回得到加密后的字符串进行解码然后进行64位的编码
    return base64.b64encode(cipher.encrypt(raw.encode('utf-8'))).decode('utf8')


# AES/ECB/PKCS5模式解密--签名解密方式
def AesECBDecrypt(data, keySecret):
    #首先对已经加密的字符串进行解码
    enc = b64decode(data)
    #通过key值，使用ECB模式进行解密
    cipher = AES.new(keySecret.encode('utf-8'), AES.MODE_ECB)
    return unpad(cipher.decrypt(enc)).decode('utf8')


# HMAC256-BASE64加密
# https://blog.csdn.net/DH2442897094/article/details/112224687
def HmacSha256AndBase64(s1, s2, spKey):
	#sha256加密有2种
    # hsobj = sha256(key.encode("utf-8"))
    # hsobj.update(data.encode("utf-8"))
    # print(hsobj.hexdigest().upper())
    # print(s1)
    # print(s2)
    # print(spKey)
    # s = s1+s2
    # data = s.encode('utf-8')
    sByteSlice = s1.encode('utf-8')+s2.encode('utf-8')
    return base64.b64encode(hmac.new(spKey.encode('utf-8'), sByteSlice,digestmod=sha256).digest()).decode("utf-8")
    # h =  hmac.new(spKey.encode('utf-8'), data, digestmod=sha256).

