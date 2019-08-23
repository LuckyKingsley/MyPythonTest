#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2019/8/23 10:39
#@Author: Kingsley
#@File  : test19082305.py

from enum import Enum, unique

# 注意的一点是 ，
# member.value 是自动赋给成员的 int类型的常量，
# 默认是从 1 开始的。而且 Enum 的成员均为单例（Singleton），并且不可实例化，不可更改
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

# @unique 装饰器可以帮助我们检查保证没有重复值
@unique
class Month(Enum):
    Jan = 'January'
    Feb = 'February'
    Mar = 'March'
    Apr = 'April'
    May = 'May'
    Jun = 'June'
    Jul = 'July'
    Aug = 'August'
    Sep = 'September '
    Oct = 'October'
    Nov = 'November'
    Dec = 'December'




if __name__ == '__main__':
    print(Month.Jan, '----------',
          Month.Jan.name, '----------', Month.Jan.value)
    for name, member in Month.__members__.items():
        print(name, '----------', member, '----------', member.value)



# 遍历枚举类型
# for name, member in Month.__members__.items():
#     print(name, '---------', member, '----------', member.value)

# 直接引用一个常量
# print('\n', Month.Jan)

