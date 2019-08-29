#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time: 2019/8/29 14:02
# @File: taobao.py
# Author: Kingsley

# 实现淘宝登录

import json

import requests

session = requests.Session()
user_name = '金金1313'
timeout = 3
password = 'jin'


# 填写完姓名后判断是否要弹出’拖拽验证框‘
def login_whether_need_code():
    url = 'https://login.taobao.com/member/request_nick_check.do?_input_charset=utf-8'
    request_headers = {
        'Referer': 'https://login.taobao.com/member/login.jhtml?spm=a21bo.2017.201864-2.d1.5af911d9LfgCQQ'
                   '&f=top&redirectURL=http%3A%2F%2Fwww.taobao.com%2F',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
    }
    form_data = {
        'username': user_name,
        'ua': '120#bX1bSTfypnfVjQbwivYfysbfbconF5qRYJe7+qRvyNQd7X92ZOjJuJPhjTj9lx3fjQyLqXYWQ1YCj4wyKi5ksuJhFTBLy'
              'utFmr2Wc74ksaQnWO0j5hhfXW73Qhx9Z+Lh3W/5jbdKm5+T+vRSpCCMLGC/EvFteuT27StYxbLgmWv5AXhEYNKR1QkRMcFhnUu'
              '5qE87j49YmPgMR2XcUHw/bIC5MseHH51MKxQSYv7xHOdxdDOEq+mwJJ2JTbDSCC0xPEubPU9/EqeX1IX1TjvPcvUebvbt7hNyq'
              'yMYSbh6Xq/Wmpbbg8GPXPc/bbSaGcMPxcnb/ikOEqP/ybYb75UyP9V5WQv54cuI7bxYg6ikMx38XIR80/1FFmJuh2NfFiXN0yaI'
              'yiRdeG04o+4Kv+pVqF+1qRaEdHBCGTg1PW8lc74++ollmXuGrrs27qOS9UzJ7G8eACz5ojj3h+jFh/eTX2joLNhwqvndCiXsbhtz'
              'ZlwtC7a8DQEQYzqpj4TmL4IEG4xc374SLsvgz/4oH801fL1A6Xx1GLr2lemN4mKzwGJXKxQpRd2FsxXKd2YUh0TpLUtMoZi5+Ww3'
              'XgbF5oMnfHc3ef02YVo6aOBc+//rD+1Xdd7wq/XI60rYESJPbPVDqasLNWuE7wLuX3Qhg0+uSD/JkyRfPB5fZ2kCXwYbx7EsXcmyo'
              'VBE0g1Yk9kULh0iOKjm8KWECtkLCwZKr7jxMJl8zd8t9mPVwqAj+1AOkFUhYQWutNaw7DrXWhjngc8+aMsdNmORAO6lHD8AiKVMoD'
              'Xgk83T5egXsQ+/zVdnP6maTHMzL6AWwPdjKKndK+mjxWPcTSBi40tgm5oJ/cBUo9aiGMsuhKs/LYQJUjgCnDpHoSZt8ZTQl7qaJC28'
              'GGw9HZTe0bJH4yHQ2IsxxPDAYj4SRQPcSG+6Cv=='
    }

    try:
        r = session.post(url, headers=request_headers, data=form_data, timeout=timeout)
        r.raise_for_status()
    except:
        print(r'判断是否要弹出’拖拽验证框‘失败')

    print(r.text)
    json_result = json.loads(r.text)
    if 'needcode' in json_result and 'false' == json_result['needcode']:
        return True
    else:
        return False


# 发送姓名密码获取token
def login_post_name_password():
    url = 'https://login.taobao.com/member/login.jhtml?redirectURL=http%3A%2F%2Fwww.taobao.com%2F'
    request_headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,'
                  'image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Connection': 'keep-alive',
        'Referer': 'https://login.taobao.com/member/login.jhtml?redirectURL=http%3A%2F%2Fwww.taobao.com%2F',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
        'Origin': 'https://login.taobao.com',
        'Upgrade-Insecure-Requests': '1'
    }
    form_data = {
        'ncoSig': '05lXxnxdScFJ2253v5luDa14-0KXyHghpBXyCv7pmQVgSO2yb2HAmVLTTBVAhu'
                  'Q51S7Fwkv1LNvXqDGy5hYjCC_ZvludE4TtWDA2dWePwDNfKnZo80SbwnK5XgQA'
                  'Y7Nn8yeptxMqj-1QtCHEtaQc-h1ywp4gecIBcsnZd40hO1cFcm3KoKij9Q8YP8'
                  'CF_dJZ_5fynS1gIAkPl5mwD8tRPcdK0IHYH7JEAEVXyxlPmwP6pXzt-LHE5cT5'
                  'iyE_4O2cEKhtPnbpYKk_R7ucaWSAS06SRAzc_LV31Ca6jvzATXQs2ltjiupHIx'
                  'TUuKgxrdIFRYCXKTVQtVzk4kg4UopNyGSXzIA0hfHwzIXGf8Zn4gQft-bl-yDnC'
                  'bLxta5_Oxmqhkm5gLxuVJNZiCO5YzonEkwMF45sqPVVzTbri7MpDPWnOZaykPHIAQSjiRuyvIEpv1',
        'ncoSessionid': '01c4zZeRV69zIzXC848cQQyZe336nOzW6I6ziBob5XqBEYNU_OxcoITO0POQBpMDertcQWjI11z'
                        'KBZFmPrSKNJrlzLSJhqM3-RF6wOcd0zzHGlf61ZL-d6LVKp9NdJoX6zYi5gYDA6c1hFyouTBMC0'
                        'ixrJL7C-W9hBJ4qyqb-ZK2eN6opq_v4P8Ppt5luJxOKW',
        'ncoToken': '008ea5639cd4bc75f82c070064e9a0bbb764b3cf',
        'slideCodeShow': 'true',
        'useMobile': 'false',
        'lang': 'zh_CN',
        'loginsite': '0',
        'newlogin': '0',
        'TPL_redirect_url': 'http://www.taobao.com/',
        'from': 'tbTop',
        'fc': 'default',
        'style': 'default',
        'keyLogin': 'false',
        'qrLogin': 'true',
        'newMini': 'false',
        'newMini2': 'false',
        'loginType': '3',
        'gvfdcname': '10',
        'sub': 'false',
        'TPL_password_2': '4a2fca49f35a358db20998569e5df666eda98d845fe0093285f323916074'
                          'c127dda5b545106f8e989de21e50c11eceb7d6524abd12bee3205ff7e6075'
                          '4c469651d1261f3ebba97df42793473b5f07c0cb36f714ba274da8695c930'
                          'a5a7b7e192dbf4422fded6c989f4967210f8f68ca44a88dfecbe83ca90b836e34f068f2103',
        'loginASR': '1',
        'loginASRSuc': '1',
        'oslanguage': 'zh-CN',
        'sr': '1920*1080',
        'naviVer': 'chrome|73.0368386',
        'osACN': 'Mozilla',
        'osAV': '5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
        'osPF': 'Win32',
        'appkey': '00000000',
        'mobileLoginLink': 'https://login.taobao.com/member/login.jhtml'
                           '?spm=a21bo.2017.201864-2.d1.5af911d9LfgCQQ&f=top'
                           '&redirectURL=http://www.taobao.com/&useMobile=true',
        'showAssistantLink': 'false',
        'um_token': 'TFDB928CF46E18C9412EC065CE46AE9DDD7E29135F87DDE84E5897BAFC0',
        'ua': '120#bX1bSXSiBLhY2GYA+1GSx+hRbcLyGsZAUH7lZk4xDzKiJMizpbA/CkmYVcRPDuHm'
              '4U+5RkQwifbNc1pGmaRD7fMlxdcU7LbMUa1+9hLik7Yxl6ykj7CL6mQzuIbWb/5vgt7k'
              'rIiWWY9m7soS6eglgntdfbwVQFBcDOAf6Ta0J1pzqtBz3i3/2PQFn84Laey7QTdpDRnEw'
              '1YW1Q+xSL01+PEpO46oGg8WE/amHcH83pJPACzilMhdjBLEWM/11NhMG2HyRonqM8boYE'
              'XSIZb0zyA74/oT3O3nZoS6TW3SIRMfNht4WD7xPfS5TN07VXFWAP4etLjjqoP0s7W7F2/T'
              'xxufB/zpErVlRhnHDJ6w6815QucfxvUF2eLxm+j6KiQPMhZ1I13U/Qlz0gv1gS5AqXdfLE'
              'Me6fC8ar8Y2o498IHcr31vHedX3xCd/rIIKrNw1bRNuI7F+oYwU5Tmzl4mEAuLY2LJCgn8'
              'MACVfJsZuzHeeJQKI4YUmuCNn3H/JGW0+dscxtI5OVBX7mc3XVYUArl7JzMNbukxp4Q6Ws'
              'Shb/WsYkYRVRxJRdSQZybUsEFUIzBvGZNS/R7Xi78ZPQSu2z7tqox+y84+SThXi1pyb4Lc'
              '65qTfYyDgJAvf/vW8DK4AACHByjgi6kPcuBnewKsAwwW4BBiKgIBc1WjAz9cHKeBiCyNRe'
              'mEhz83Guz4/1A5mE+ryVbAgnjNjhKx47wpmNzW0+0NELUuvA5MQwZn33zyGxwDfAG4Knh3'
              'PjTrwCNhYv7DHOdxdDOEqKXP9+6bwcEcTLhIPXubfgabPqPto1bS75GPNqP/bbYtYW3PyXK'
              'Sb5T0Nqe/nvbw7UGPWWl/bbXDZdVdo174c6cyb1G74JiugnZgDYbtZAcDxahgDemglarE8M'
              'OuL0UfRCGAyRF+9JhgEPuJ3QRC6m8fAuX2p8ObsWxdv7tZZRyPvgUM3TKySPF/AOCJJFVyMq'
              '1/3E290V8diKxLZj6vB7Dcd36DWzGBmDv686NNL1ZCxR0oFgDvAFyn+VEkYpEpGz7xX0+1W66'
              'Nhoa9oHohIbIbHA2CZpOsGbjil57zkB3UH3y+2s6ZiVFtc0dXKdGeyx5THr8EdZHq085ZIX3M'
              'fxqanwSZzgFrmWOsfGkk+UHK0gplTbTXaLtTJEjgV1B174UUAtuGwjgLsXzLi3b4Ekmo6EPbx'
              '6m/GaoNTg9MzpHGkrJE2EKDJIxqOeWSUadvjCZJtaPBGEuYIn5dTXHitaNPTxTUoW+yVT+rGrF'
              'p3tl6gSpqbX7UrzA0k+vWO14/JhWNKz3gkLV/nV74EotXzjDJVVDzlb955GjrkKY1EuoKxQYGO'
              '5EHX5ntwz3p6cF+kEt7iDevGKv526M/OB6j2HCT6rSr5oSEdUZ8VKGMjm6gYCLJyPGqpb=='
    }

    try:
        r = session.post(url, headers=request_headers, data=form_data, timeout=timeout)
        r.raise_for_status()
    except:
        print('发送姓名密码获取token失败')

    print(r.text)


if __name__ == '__main__':
    # login_whether_need_code()
    login_post_name_password()
