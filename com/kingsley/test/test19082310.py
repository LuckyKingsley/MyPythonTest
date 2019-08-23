#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2019/8/23 14:43
#@Author: Kingsley
#@File  : test19082310.py


# 如果是这样写的话，Python 就会用元类来创建类 MyObject。
# 当你写下 class MyObject(object)，但是类对象 MyObject 还没有在内存中创建。
# Python 会在类的定义中寻找 __metaclass__ 属性，如果找到了，Python 就会用它来创建类 MyObject，
# 如果没有找到，就会用内建的 type 函数来创建这个类
# class Foo(Bar):
#     __metaclass__ = something…
#     pass
# 首先判断 Foo 中是否有 __metaclass__ 这个属性？
# 如果有，Python 会在内存中通过 __metaclass__ 创建一个名字为 Foo 的类对象（注意，这里是类对象）。
# 如果 Python 没有找到__metaclass__ ，它会继续在 Bar（父类）中寻找__metaclass__ 属性，并尝试做和前面同样的操作。
# 如果 Python在任何父类中都找不到 __metaclass__ ，它就会在模块层次中去寻找 __metaclass__ ，并尝试做同样的操作。
# 如果还是找不到` metaclass` ,Python 就会用内置的 type 来创建这个类对象
# 元类会自动将你通常传给‘type’的参数作为自己的参数传入
def upper_attr(future_class_name, future_class_parents, future_class_attr):
    '''返回一个类对象，将属性都转为大写形式'''
    #  选择所有不以'__'开头的属性
    attrs = ((name, value) for name, value in future_class_attr.items() if not name.startswith('__'))

    # 将它们转为大写形式
    uppercase_attr = dict((name.upper(), value) for name, value in attrs)

    # 通过'type'来做类对象的创建
    return type(future_class_name, future_class_parents, uppercase_attr)


__metaclass__ = upper_attr
#  这会作用到这个模块中的所有类


class Foo(object):
    # 我们也可以只在这里定义__metaclass__，这样就只会作用于这个类中
    bar = 'bip'


print(hasattr(Foo, 'bar'))
# 输出: False
print(hasattr(Foo, 'BAR'))
# 输出:True

f = Foo()
print(f.BAR)
# 输出:'bip'