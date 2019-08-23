#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2019/8/23 15:03
# @Author: Kingsley
# @File  : test19082311.py


# 线程间通信
from queue import Queue
from threading import Thread

isRead = True


def write(q):
    # 写数据进程
    for value in ['两点水', '三点水', '四点水']:
        q.put(value)
        print('写进 Queue 的值为：{0}'.format(value))


def read(q):
    # 读取数据进程
    while isRead:
        value = q.get(True)
        print('从 Queue 读取的值为：{0}'.format(value))


if __name__ == '__main__':
    q = Queue()
    t1 = Thread(target=write, args=(q,))
    t2 = Thread(target=read, args=(q,))
    t1.start()
    t2.start()
