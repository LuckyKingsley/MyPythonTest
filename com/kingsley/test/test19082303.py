#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2019/8/23 10:09
#@Author: Kingsley
#@File  : test19082303.py

# 自定义不可变容器类型	需要定义 __len__ 和 __getitem__ 方法
# 自定义可变类型容器	在不可变容器类型的基础上增加定义 __setitem__ 和 __delitem__
# 自定义的数据类型需要迭代	需定义 __iter__
# 返回自定义容器的长度	需实现 __len__(self)
# 自定义容器可以调用 self[key] ，如果 key 类型错误，抛出TypeError ，如果没法返回key对应的数值时,该方法应该抛出ValueError	需要实现 __getitem__(self, key)
# 当执行 self[key] = value 时	调用是 __setitem__(self, key, value)这个方法
# 当执行 del self[key] 方法	其实调用的方法是 __delitem__(self, key)
# 当你想你的容器可以执行 for x in container: 或者使用 iter(container) 时	需要实现 __iter__(self) ，该方法返回的是一个迭代器

class FunctionalList:

    def __init__(self, values=None):
        if values is None:
            self.values = []
        else:
            self.values = values

    def __len__(self):
        return len(self.values)

    def __getitem__(self, key):
        return self.values[key]

    def __setitem__(self, key, value):
        self.values[key] = value

    def __delitem__(self, key):
        del self.values[key]

    def __iter__(self):
        return iter(self.values)

    def __reversed__(self):
        return  FunctionalList(reversed(self.values))

    def append(self, value):
        self.values.append(value)

    def head(self):
        # 获取第一个元素
        return self.values[0]

    def tail(self):
        # 获取第一个元素之后的所有元素
        return self.values[1:]

    def init(self):
        # 获取最后一个元素之前的所有元素
        return self.values[:-1]

    def last(self):
        # 获取最后一个元素
        return self.values[-1]

    def drop(self, n):
        # 获取所有元素，除了前N个
        return self.values[n:]

    def take(self, n):
        # 获取前N个元素
        return self.values[:n]