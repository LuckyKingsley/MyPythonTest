#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2019/8/23 10:30
#@Author: Kingsley
#@File  : test19082304.py


class Number(object):
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        print('__eq__')
        return self.value == other.value

    def __ne__(self, other):
        print('__ne__')
        return self.value != other.value

    def __lt__(self, other):
        print('__lt__')
        return self.value < other.value

    def __gt__(self, other):
        print('__gt__')
        return self.value > other.value

    def __le__(self, other):
        print('__le__')
        return self.value <= other.value

    def __ge__(self, other):
        print('__ge__')
        return self.value >= other.value


if __name__ == '__main__':
    num1 = Number(2)
    num2 = Number(3)
    print('num1 == num2 ? --------> {} \n'.format(num1 == num2))
    print('num1 != num2 ? --------> {} \n'.format(num1 == num2))
    print('num1 < num2 ? --------> {} \n'.format(num1 < num2))
    print('num1 > num2 ? --------> {} \n'.format(num1 > num2))
    print('num1 <= num2 ? --------> {} \n'.format(num1 <= num2))
    print('num1 >= num2 ? --------> {} \n'.format(num1 >= num2))


# __add__(self, other)	实现了加号运算
# __sub__(self, other)	实现了减号运算
# __mul__(self, other)	实现了乘法运算
# __floordiv__(self, other)	实现了 // 运算符
# ___div__(self, other)	实现了/运算符. 该方法在 Python3 中废弃. 原因是 Python3 中，division 默认就是 true division
# __truediv__(self, other)	实现了 true division. 只有你声明了 from __future__ import division 该方法才会生效
# __mod__(self, other)	实现了 % 运算符, 取余运算
# __divmod__(self, other)	实现了 divmod() 內建函数
# __pow__(self, other)	实现了 ** 操作. N 次方操作
# __lshift__(self, other)	实现了位操作 <<
# __rshift__(self, other)	实现了位操作 >>
# __and__(self, other)	实现了位操作 &
# __or__(self, other)	实现了位操作 `	`
# __xor__(self, other)	实现了位操作 ^