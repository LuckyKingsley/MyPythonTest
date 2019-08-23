#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2019/8/23 15:03
# @Author: Kingsley
# @File  : test19082311.py


# 在 Python 中，如果一个函数使用了和全局变量相同的名字且改变了该变量的值，那么该变量就会变成局部变量，
# 那么就会造成在函数中我们没有进行定义就引用了，所以会报错误

time = 0


def insert_time(min):
    global time
    time = time + min
    return time


# print(insert_time(2))
# print(insert_time(10))


# 闭包来解决全局变量问题
def study_time(time):
    def insert_time(min):
        nonlocal time
        time = time + min
        return time

    return insert_time


f = study_time(time)
print(f(2))
print(time)
print(f(10))
print(time)
