#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time: 2019/8/27 9:50
# @File: youkudanmu.py
# Author: Kingsley


import requests
import json
import os
import time
import random


def spider_youku_danmu(danmu_file, mat=0):
    """优酷弹幕抓取"""

    url = 'https://service.danmu.youku.com/list?jsoncallback=jQuery1112047883400435428625_1566870384419' \
          '&mat=%s&mcount=1&ct=1001&iid=1064640070&aid=455775&cid=85&lid=0&ouid=0&_=1566870384443' % mat
    kv = {'Referer': 'https://v.youku.com/v_show/id_XNDI1ODU2MDI4MA==.html'
                     '?scm=20140719.manual.2540.video_XNDI1ODU2MDI4MA%3D%3D&spm=a2ha1.12675304.m_2540_c_8246.d_4',
          'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                        'Chrome/73.0.3683.86 Safari/537.36'}

    try:
        r = requests.get(url, headers=kv)
        r.raise_for_status()
        json_start_index = r.text.index('(') + 1
        json_obj = json.loads(r.text[json_start_index:-2])
        json_obj_results = json_obj['result']

        if not json_obj['count']:
            return 0

        for json_obj_result in json_obj_results:
            with open(danmu_file, 'a+') as file:
                file.write(json_obj_result['content'] + '\n')
                print(json_obj_result['content'])
        return 1
    except:
        print('爬取优酷失败')
        return -1


def batch_spider():
    danmu_file = 'youku_danmu.txt'
    if os.path.exists(danmu_file):
        os.remove(danmu_file)
    i = 0
    while spider_youku_danmu(danmu_file, i):
        time.sleep(random.random() * 5)
        i += 1


if __name__ == '__main__':
    batch_spider()