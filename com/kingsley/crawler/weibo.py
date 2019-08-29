#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time: 2019/8/27 14:58
# @File: weibo.py
# Author: Kingsley

import collections
import csv
import json
import re
from pyecharts.charts import Pie
from pyecharts import options

import requests

since_id = 0
session = requests.Session()
phone = '13215603102'
password = 'jinXIN123'


# 根据手机号获取验证码
def login_weibo_getsms():
    url = 'https://m.weibo.cn/api/login/sendsms'
    kv = {
        'Referer': 'https://m.weibo.cn/login?backURL=https%3A%2F%2Fm.weibo.cn%2F',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/73.0.3683.86 Mobile Safari/537.36'
    }
    data = {
        'phone': phone,
        'st': 'false',
    }
    try:
        r = session.post(url, headers=kv, data=data)
        r.raise_for_status()
    except:
        print('获取验证码失败')

    return json.loads(r.text)


# 根据验证码登陆
def login_weibo_sms(sms):
    url = 'https://m.weibo.cn/api/login/smsLogin'
    kv = {
        'Referer': 'https://m.weibo.cn/login?backURL=https%3A%2F%2Fm.weibo.cn%2F',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36'
                      ' (KHTML, like Gecko) Chrome/73.0.3683.86 Mobile Safari/537.36'
    }
    data = {
        'phone': phone,
        'st': 'false',
        'code': sms
    }
    try:
        r = session.post(url, headers=kv, data=data)
        r.raise_for_status()
    except:
        print('登陆失败')

    print(r.text)
    return json.loads(r)


# 根据账号密码登陆
def login_weibo_password():
    url = 'https://passport.weibo.cn/sso/login'
    kv = {
        'Referer': 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=https://m.weibo.cn/',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/73.0.3683.86 Mobile Safari/537.36'
    }
    data = {
        'username': phone,
        'password': password,
        'savestate': '1',
        'r': 'https://m.weibo.cn/',
        'ec': '0',
        'pagerefer': 'https://m.weibo.cn/login?backURL=https%3A%2F%2Fm.weibo.cn%2F',
        'entry': 'mweibo',
        'mainpageflag': '1'

    }
    try:
        r = session.post(url, headers=kv, data=data)
        r.raise_for_status()
    except:
        print('登陆失败')

    print(r.text)
    return json.loads(r.text)


# 获取个人信息1
def personnal_information1(uid):
    url = 'https://m.weibo.cn/profile/info?uid=' + uid
    kv = {
        'Referer': 'https://m.weibo.cn/profile/' + uid,
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/73.0.3683.86 Mobile Safari/537.36'
    }
    try:
        r = session.get(url, headers=kv)
        r.raise_for_status()
    except:
        print('获取个人信息失败')

    print(r.text)
    return json.loads(r.text)


# 获取个人信息2
def personnal_information2(uid):
    url = 'https://weibo.cn/' + uid + '/info'
    kv = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
    }
    try:
        r = session.get(url, headers=kv)
        r.raise_for_status()
    except:
        print('获取个人信息失败')

    # print(r.text)
    return r.text


# 处理个人信息格式
def handle_personal_information(text):
    information = re.findall('<div class="tip">基本信息</div><div class="c">(.*?)</div>', text)
    information_kvs = information[0].split('<br/>')
    # print(information)
    # print(information_kvs)

    information_dict = {'昵称': None, '性别': None, '地区': None, '生日': None}

    for info in information_kvs:
        if info.startswith('昵称'):
            information_dict['昵称'] = info.split(":")[1]
        if info.startswith('性别'):
            information_dict['性别'] = info.split(":")[1]
        if info.startswith('地区'):
            information_dict['地区'] = info.split(":")[1]
        if info.startswith('生日'):
            information_dict['生日'] = info.split(":")[1]

    return information_dict


# 获取周杰伦超话内容
def spider_weibo():
    global since_id
    url = 'https://m.weibo.cn/api/container/getIndex?containerid=1008087a8941058aaf4df5147042ce104568da_-_feed' \
          '&luicode=10000011&lfid=100103type%3D1%26q%3D%E5%91%A8%E6%9D%B0%E4%BC%A6%E8%B6%85%E8%AF%9D'
    kv = {
        'Referer': 'https://m.weibo.cn/p/index?containerid=1008087a8941058aaf4df5147042ce104568da'
                   '&luicode=10000011&lfid=100103type%3D1%26q%3D%E5%91%A8%E6%9D%B0%E4%BC%A6%E8%B6%85%E8%AF%9D',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/73.0.3683.86 Mobile Safari/537.36'
    }

    try:
        if since_id:
            r = requests.get(url + '&since_id=' + since_id, headers=kv)
        else:
            r = requests.get(url, headers=kv)
        r.raise_for_status()
    except:
        print('false')

    json_weibo = json.loads(r.text)
    json_weibo_cards = json_weibo['data']['cards']
    for card in json_weibo_cards:
        if 'card_group' in card:
            for card_group in card['card_group']:
                if 'mblog' in card_group:
                    with open('weibo.csv', mode='a', encoding='utf-8') as csvfile:
                        text = personnal_information2(str(card_group['mblog']['user']['id']))
                        information_dict = handle_personal_information(text)

                        column = []
                        column.append(str(card_group['mblog']['user']['id']))
                        column.append(information_dict['昵称'])
                        column.append(information_dict['性别'])
                        column.append(information_dict['地区'])
                        column.append(information_dict['生日'])
                        column.append(card_group['mblog']['id'])
                        column.append(
                            re.compile(r'<[^>]+>', re.S).sub(' ', card_group['mblog']['text'].replace('周杰伦超话', ' ')))

                        csv_witer = csv.writer(csvfile)
                        csv_witer.writerow(column)

                        r_since_id = card_group['mblog']['id']
                        if since_id:
                            since_id = r_since_id if since_id > r_since_id else since_id
                        else:
                            since_id = r_since_id


def read_csv_to_dict(index) -> dict:
    with open('weibo.csv', 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        column = []
        for columns in reader:
            if len(columns) > 0:
                column.append(columns[index])
        dic = collections.Counter(column)
        # 删除空字符串
        if '' in dic:
            dic.pop('')
        print(dic)
        return dic


if __name__ == '__main__':
    """"""
    # json_result = login_weibo_getsms()
    # print(json_result)
    # if ('ok' in json_result and 1 == json_result['ok']) and ('isreg' in json_result and 'true' == json_result['isreg']):
    #     print('发送验证码成功')

    # login_weibo_sms('339317')

    """"""
    # json_reuslt = login_weibo_password()
    # if 'retcode' in json_reuslt and 20000000 == json_reuslt['retcode']:
    #     uid = json_reuslt['data']['uid']
    #     # json_personnal_information = personnal_information1(uid)
    #     text = personnal_information2(uid)
    #     birthday = re.findall('<p id="J_birthday" style="display:none;">(.*?)</p></div>', text)
    #     location = re.findall('<p id="J_location" class="J_label"[^>]*>([^<]*)</p>', text)
    #     name = re.findall('<p id="J_name" class="J_label" isCompany="">(.*?)</p></div>', text)
    #     agender = re.findall('<span class="L-selected-select">(.*?)</span></div>', text)
    # else:
    #     print('登陆失败')
    """"""

    # if os.path.exists('weibo.csv'):
    #     os.remove('weibo.csv')
    # for i in range(1000):
    #     time.sleep(random.random() * 3)
    #     print('第%d页' % (i + 1))
    #     spider_weibo()

    """"""
    dic = read_csv_to_dict(2)
    # 生成二维数组
    gender_count_list = [list(z) for z in zip(dic.keys(), dic.values())]
    print(gender_count_list)
    pie = (
        Pie()
        .add('', gender_count_list)
        .set_colors(['red', 'blue'])
        .set_global_opts(title_opts=options.TitleOpts(title='性别分析'))
        .set_series_opts(label_opts=options.LabelOpts(formatter='{b}: {c}'))
    )
    pie.render('gender.html')
