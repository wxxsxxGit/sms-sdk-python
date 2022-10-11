# -*- coding: utf-8 -*-
import random

def RandString(randomlength=16):
    """
    生成一个指定长度的随机字符串
    """
    random_str =''
    base_str ='ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz0123456789'
    length =len(base_str) -1
    for i in range(randomlength):
      random_str +=base_str[random.randint(0, length)]
    return random_str


fillLetter  = "a"


def NormalizeKey(key):
    if len(key) >= 16:
        return key[0:16]
    length = len(key)
    fillLength = 16 - length
    return fillLetter * fillLength + key
