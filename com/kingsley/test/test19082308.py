#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2019/8/23 11:37
# @Author: Kingsley
# @File  : test19082308.py

def printHello(self, name='Py'):
    # 定义一个打印 Hello 的函数
    print('Hello,', name)


# 创建一个 Hello 类
# type函数是一个元类，就是 Python 在背后用来创建所有类的元类
Hello = type('Hello', (object,), dict(hello=printHello))

# 实例化 Hello 类
h = Hello()
# 调用 Hello 类的方法
h.hello()
# 查看 Hello class 的类型
print(type(Hello))
# 查看实例 h 的类型
print(type(h))