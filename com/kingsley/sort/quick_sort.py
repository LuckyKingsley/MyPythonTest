#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time: 2019/8/29 15:31
# @File: quick_sort.py
# Author: Kingsley


# 快速排序
def quick_sort(arr):
    """快速排序"""
    if len(arr) < 2:
        return arr
    # 选取基准，随便选哪个都可以，选中间的便于理解
    mid = arr[len(arr) // 2]
    # 定义基准值左右两个数列
    left, right = [], []
    # 从原始数组中移除基准值
    arr.remove(mid)
    for item in arr:
        # 大于基准值放右边
        if item >= mid:
            right.append(item)
        else:
            # 小于基准值放左边
            left.append(item)
    # 使用迭代进行比较
    return quick_sort(left) + [mid] + quick_sort(right)


print(quick_sort([3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]))