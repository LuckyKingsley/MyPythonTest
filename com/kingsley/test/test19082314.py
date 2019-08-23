#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2019/8/23 15:03
# @Author: Kingsley
# @File  : test19082311.py


# Event 对象用于线程间通信
import threading


class mThread(threading.Thread):
    def __init__(self, threadname):
        threading.Thread.__init__(self, name=threadname)

    def run(self):
        # 使用全局Event对象
        global event
        # 判断Event对象内部信号标志
        if event.isSet():
            event.clear()
            event.wait()
            print(self.getName())
        else:
            print(self.getName())
            # 设置Event对象内部信号标志
            event.set()

# 生成Event对象
event = threading.Event()
# 设置Event对象内部信号标志
event.set()
t1 = []
for i in range(10):
    t = mThread(str(i))
    # 生成线程列表
    t1.append(t)

for i in t1:
    # 运行线程
    i.start()