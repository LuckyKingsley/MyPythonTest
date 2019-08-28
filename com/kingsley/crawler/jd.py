#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time: 2019/08/26 21:30
# @File: jd.py
# Author: Kingsley

# python网络库
# Python3: httplib2、urllib、urllib3、requests

import json
import os
import random
import time

import jieba
import matplotlib.pyplot as plt
import numpy as np
import requests
from PIL import Image
from wordcloud import WordCloud


# httpbin.org是一个测试http请求的网站，能正常回应请求
def http_bin_test():
    try:
        r = requests.head('http://httpbin.org/get')
        r.raise_for_status()  # raise_for_status会判断返回状态码，如果4XX或5XX则会抛出异常
        print(r.text[:500])
    except:
        print('测试失败')


def spider_jd(comment_file_path, page=0):
    """爬取京东商品页评论"""
    url = 'https://sclub.jd.com/comment/productPageComments.action' \
          '?callback=fetchJSON_comment98vv4654&productId=1263013576&score=0' \
          '&sortType=5&page=%s&pageSize=10&isShadowSku=0&fold=1' % page
    kv = {'Referer': 'https://item.jd.com/1263013576.html', 'user-agent': 'Mozilla/5.0'}
    try:
        r = requests.get(url, headers=kv)
        r.raise_for_status()  # raise_for_status会判断返回状态码，如果4XX或5XX则会抛出异常
        print('某东评论数据：{}'.format(r.text[26:-2]))
        r_json_obj = json.loads(r.text[26:-2])
        r_json_comments = r_json_obj['comments']

        for r_json_comment in r_json_comments:
            with open(comment_file_path, 'a+') as file:
                file.write(r_json_comment['content'] + '\n')
                print('具体评论为：{}'.format(r_json_comment['content']))

    except:
        print('爬取失败')


def batch_spider():
    # 写如数据前先清空之前的数据
    comment_file_path = 'jd_comment.txt'
    if os.path.exists(comment_file_path):
        os.remove(comment_file_path)
    for i in range(10):
        spider_jd(comment_file_path, i)
        time.sleep(random.random() * 5)


def cut_word():
    """对数据分词"""
    with open('jd_comment.txt') as file:
        comment_txt = file.read()
        word_list = jieba.cut(comment_txt, cut_all=True)
        wl = " ".join(word_list)
        print(wl)
        return wl


def create_word_cloud():
    """生成词云"""
    wc_mask = np.array(Image.open('qq.jpg'))
    wc = WordCloud(background_color="white", max_words=2000, mask=wc_mask, scale=4,
                   max_font_size=50, random_state=42, font_path='C:\\WINDOWS\\Fonts\\simfang.ttf')
    wc.generate(cut_word())

    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.figure()
    plt.show()


if __name__ == '__main__':
    # http_bin_test()
    batch_spider()
    # cut_word()
    create_word_cloud()
