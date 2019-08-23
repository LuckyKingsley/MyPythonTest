#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2019/8/22 15:28
#@Author: Kingsley
#@File  : test19082202.py


# class Test:
#
#     name = '刘昂点水'
#
#     def __init__(self, name, age, account):
#         self.name = name
#         self._age = age
#         self.__account = account
#
#     def prt(self):
#         print(self)
#         print(self.__class__)

class UserInfo(object):
    def __init__(self, name, age, account):
        self.name = name
        self._age = age
        self.__account = account

    def get_account(self):
        return self.__account


if __name__ == '__main__':
    userInfo = UserInfo('两点水', 23, 347073565);
    # 打印所有属性
    print(dir(userInfo))
    # 打印构造函数中的属性
    print(userInfo.__dict__)
    print(userInfo.get_account())
    # 用于验证双下划线是否是真正的私有属性
    print(userInfo._UserInfo__account)
    print()
    print(type(userInfo))
    print(getattr(userInfo, '_UserInfo__account', '找不到'))
    print(getattr(userInfo, 'get_account', '找不到'))
