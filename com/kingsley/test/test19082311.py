#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2019/8/23 15:03
# @Author: Kingsley
# @File  : test19082311.py

import threading
import time


class MyThread(threading.Thread):

    def run(self):
        for i in range(5):
            print('thread {}, @number: {}'.format(self.name, 1))
            time.sleep(1)


def main():
    print("Start main threading")

    # 创建三个线程
    threads = [MyThread() for i in range(3)]
    # 启动三个线程
    for t in threads:
        t.start()

    ############
    # 加入此段代码可使主线程在子线程运行完后再退出
    # 依次让新创建的线程执行 join
    for t in threads:
        t.join()
    ############

    print("End Main threading")


if __name__ == '__main__':
    main()
