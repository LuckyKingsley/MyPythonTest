#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time: 2019/8/30 16:14
# @File: xpath.py
# Author: Kingsley

# XPath (XML Path Language) 是一门在 XML 文档中查找信息的语言，可用来在 XML 文档中对元素和属性进行遍历

import requests
from lxml import etree


def zhihu_shouye():
    url = 'https://www.zhihu.com/signin?next=%2F'
    kv = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,'
                  'image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'cookie': '_xsrf=reeLLeMIPMM9youRG3xCVQwgKS5nLo11; _zap=f853da09-38d6-429a-ad97-d00328f0758d;'
                  ' d_c0="ADCh4tkz-A-PToAlQy8VYLTR8Dt6l7L2O3U=|1567134628"; capsion_ticket="2|1:0|10:'
                  '1567393819|14:capsion_ticket|44:YzI4YWVmZDdiMzUxNGE2OGE0MjczNTBjY2NiZmMyOWI=|b67c5a'
                  '351153c65bf0f000ecd332b6d86d8d7acfbac7be1dda15c6206197fbb9"; tgw_l7_route=4860b599c6'
                  '644634a0abcd4d10d37251'
    }
    data = {
        'next': '/'
    }

    try:
        r = requests.get(url, headers=kv, data=data)
        r.raise_for_status()
    except:
        print('shibai')

    print(r.text)
    # 利用etree.HTML，将字符串解析为HTML文档
    html = etree.HTML(r.text)
    # 按字符串序列化HTML文档
    result = etree.tostring(html, encoding='gbk')
    print(result)


zhihu_shouye()