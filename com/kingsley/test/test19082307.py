#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2019/8/23 11:22
#@Author: Kingsley
#@File  : test19082307.py
#可以把类理解成也是一种对象
class ObjectCreator(object):
    pass


def echo(ob):
    print(ob)


mobject = ObjectCreator()
print(mobject)
# 可以直接打印一个类，因为它其实也是一个对象
print(ObjectCreator)
# 可以直接把一个类作为参数传给函数（注意这里是类，是没有实例化的）
echo(ObjectCreator)
# 也可以直接把类赋值给一个变量
objectCreator = ObjectCreator
print(objectCreator)