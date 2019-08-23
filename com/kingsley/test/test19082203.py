#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2019/8/22 16:00
#@Author: Kingsley
#@File  : test19082203.py


class UserInfo(object):
    lv = 5

    def __init__(self, name, age, account):
        self.name = name
        self._age = age
        self.__account = account

    def get_account(self):
        return self.__account

    @classmethod
    def get_name(cls):
        return cls.lv

    @property
    def get_age(self):
        return self._age


class UserInfo2(UserInfo):
    def __init__(self, name, age, account, sex):
        super(UserInfo2, self).__init__(name, age, account)
        self.sex = sex


class UserInfo3:
    pass


# if __name__ == '__main__':
#     userInfo = UserInfo('两点水', 23, 347073565)
#     print()
#     # 打印所有属性
#     print(dir(userInfo))
#     # 打印构造函数中的属性
#     print(userInfo.__dict__)
#     print(userInfo.__init__)
#     # 直接使用类名类调用，而不是某个对象
#     print(UserInfo.lv)
#     # 像访问属性一样调用方法（注意看get_age是没有括号的）
#     print(userInfo.get_age)
#     print(UserInfo.get_account(userInfo))

if __name__ == '__main__':
    userInfo2 = UserInfo2('两点水', 23, 347073565, '男')
    print()
    # 打印所有属性
    print(dir(userInfo2))
    # 打印构造函数中的属性
    print(userInfo2.__dict__)
    print(UserInfo2.get_name())
    print(isinstance(userInfo2, UserInfo2))
    print(isinstance(userInfo2, UserInfo))

    print(dir(UserInfo3()))