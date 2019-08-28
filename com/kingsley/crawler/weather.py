#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time: 2019/8/28 9:26
# @File: weather.py
# Author: Kingsley

import requests
import json
import redis

# 调取免费天气api获取未来天气信息


def spider_weather():
    url = 'https://www.tianqiapi.com/api/?version=v1&appid=59461357&appsecret=75JsP4A1&cityid=101190101'

    try:
        r = requests.get(url)
        r.raise_for_status()
    except:
        print('false')

    print(r.text)
    weather_json = json.loads(r.text)
    redis_connector = redis.Redis()
    redis_connector.set('weather', r.text)
    print(redis_connector.get('weather'))


spider_weather()