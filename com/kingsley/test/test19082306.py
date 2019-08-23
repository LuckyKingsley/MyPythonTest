#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2019/8/23 11:04
#@Author: Kingsley
#@File  : test19082306.py
# Enum 类的枚举是不支持大小运算符的比较
# 使用 IntEnum 类进行枚举，就支持比较功能。
from enum import unique
import enum

@unique
class User(enum.IntEnum):

    Twowater = 98
    Liangdianshui = 30
    Tom = 12

Twowater = User.Twowater
Liangdianshui = User.Liangdianshui

print(Twowater == Liangdianshui, Twowater == User.Twowater)
print(Twowater is Liangdianshui, Twowater is User.Twowater)

try:
    print('\n'.join('  ' + s.name for s in sorted(User)))
except TypeError as err:
    print(' Error : {}'.format(err))