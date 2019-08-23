#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2019/8/22 15:16
# @Author: Kingsley
# @File  : user.py


def vip_lv_name(lv):
    if lv == 1:
        print(_gold_vip(lv))
    elif lv == 2:
        print(_diamond_vip(lv))


def _diamond_vip(lv):
    print('尊敬的钻石会员用户，您好')
    vip_name = 'DiamondVIP' + str(lv)
    return vip_name


def _gold_vip(lv):
    print('尊敬的黄金会员用户，您好')
    vip_name = 'GoldVIP' + str(lv)
    return vip_name
