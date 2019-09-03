#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time: 2019/9/2 14:41
# @File: earthquake.py
# Author: Kingsley


# 抓取近一年地震最频繁的地区信息

import requests
import time
import json
import csv
import collections


def spider_eqrthquake(page, timestamp):
    url = 'http://www.ceic.ac.cn/ajax/speedsearch' \
          '?num=6' \
          '&&page=%d' \
          '&&callback=jQuery18008643705767404637_1567406641545&_=%s' % (page, timestamp)
    headers = {
        'Cookie': 'PHPSESSID=abbf025cd8e4de71aab70bbd56634106; Hm_lvt_e0025cd5d35216'
                  '5f8a646ccea5beb27d=1567406642; Hm_lpvt_e0025cd5d352165f8a646ccea5beb27d=1567406813',
        'Referer': 'http://www.ceic.ac.cn/speedsearch?time=10',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
    }

    try:
        r = requests.get(url, headers=headers)
        r.raise_for_status()
    except:
        print('失败')

    json_text = json.loads(r.text[41:-1])
    json_text_shuju = json_text['shuju']
    for item in json_text_shuju:
        with open('earthquake.csv', 'a+', encoding='utf-8', newline='') as file:
            csv_wirter = csv.writer(file)
            column = []
            column.append(item['M'])
            column.append(item['O_TIME'])
            column.append(item['EPI_LAT'])
            column.append(item['EPI_LON'])
            column.append(item['EPI_DEPTH'])
            column.append(item['LOCATION_C'])
            csv_wirter.writerow(column)


def get_timestamp():
    ts = str(time.time() * 1000)
    ts = int(ts[:13])
    return ts


def read_csv():
    with open('earthquake.csv', 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        result = []
        for columns in reader:
            if len(columns) > 0:
                if columns[5].find('四川') >= 0:
                    result.append(columns)
        return len(result)


if __name__ == '__main__':
    # for i in range(58):
    #     spider_eqrthquake(i, get_timestamp())
    #
    # print('done')
    print(read_csv())