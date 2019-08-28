#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time: 2019/8/27 11:40
# @File: douban.py
# Author: Kingsley

# 分析豆瓣的登录接口并用requests库实现登录并保存cookie
# 分析豆瓣影评接口实现批量抓取数据
# 使用词云做影评数据分析

# 用session解决登陆问题

import re

import requests

# 生成session对象
session = requests.Session()
douban_comment_file = 'douban_comment.txt'


def login_douban():
    """
    登陆豆瓣
    :return:
    """
    url = 'https://accounts.douban.com/j/mobile/login/basic'
    header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                            'Chrome/73.0.3683.86 Safari/537.36',
              'Referer': 'https://accounts.douban.com/passport/login_popup?login_source=anony', }
    data = {
        'name': '13215603102',
        'password': 'jinXIN123',
        'remember': 'false'
    }

    try:
        r = session.post(url, headers=header, data=data)
        r.raise_for_status()
    except:
        print('爬取豆瓣登录接口失败')

    print(r.text)


def spider_comment():
    """
    拉取评论
    :return:
    """
    comment_url = 'https://movie.douban.com/subject/27163278/comments?start=220&limit=20&sort=new_score&status=P'
    kv = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                        'Chrome/73.0.3683.86 Safari/537.36'}

    try:
        r = session.get(comment_url, headers=kv)
        r.raise_for_status()
    except:
        print('抓取错误')

    print(r.text)
    # 使用正则提取影评内容
    comment = re.findall('<span class="short">(.*)</span>', r.text)
    for cm in comment:
        with open(douban_comment_file, 'a+') as file:
            file.write(cm + '\n')
            print(cm)


if __name__ == '__main__':
    login_douban()
    spider_comment()
