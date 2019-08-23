#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2019/8/23 14:00
#@Author: Kingsley
#@File  : test19082309.py

# 元类就是负责生成类的。
# type 就是内建的元类。也就是 Python 自带的元类。

# 整形
age = 23
print(age.__class__)
# 字符串
name = '两点水'
print(name.__class__)


# 函数
def fu():
    pass


print(fu.__class__)


# 实例
class eat(object):
    pass


mEat = eat()

print(mEat.__class__)
print(mEat.__class__.__class__)

