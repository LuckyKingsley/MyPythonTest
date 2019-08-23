#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2019/8/23 9:39
#@Author: Kingsley
#@File  : test19082302.py

# 描述器对象 (Meter、Foot) 不能独立存在, 它需要被另一个所有者类 (Distance) 所持有。
# 描述器对象可以访问到其拥有者实例的属性，比如例子中 Foot 的 instance.meter 。

class Meter(object):
    def __init__(self, value=0.0):
        self.value = float(value)

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        self.value = float(value)


class Foot(object):
    def __get__(self, instance, owner):
        return instance.meter * 3.2808

    def __set__(self, instance, value):
        instance.meter = float(value) / 3.2808


class Distance(object):
    meter = Meter()
    foot = Foot()


if __name__ == '__main__':
    d = Distance()
    print(d.meter, d.foot)
    d.meter = 1
    print(d.meter, d.foot)
    d.meter = 2
    print(d.meter, d.foot)