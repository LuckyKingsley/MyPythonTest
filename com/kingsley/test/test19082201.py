# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2019/8/21 14:51
# @Author: Kingsley
# @File  : test19082201.py



def complex1(real, img):
    pass


def complex2(real, img=0.0):
    pass


def long_function_name(var_one, var_two,
                       var_three, var_four):
    """first

    :param(1):var_one
    :param(2):var_two
    :param(3):var_three
    :param(4):var_four
    :return:null

    this is just a test docstring"""

    """second"""
    # print
    # 'Hello, ' \
    # '%s %s!' % \
    # ('Harry', 'Potter')   # print something

    a = 'Hello \'两点水\' "你好啊"'
    b = "Hello '两点水' \"你好啊\""
    # print(a)
    # print(b)

    # 可以在字符串前面加个前缀 r ，表示这是一个 raw 字符串，里面的字符就不需要转义了。
    # 但是r'...'表示法不能表示多行字符串，也不能表示包含'和"的字符串
    c = r'\--/'
    # print(c)
    d = None
    e = True
    f = False
    g = h = i = 1
    # print(g, h, i)
    j, k, l = 1, 2, 'Kingsley'
    # print(j, k, l)

    # int(x [,base ])	将x转换为一个整数
    # float(x )	将x转换到一个浮点数
    # complex(real [,imag ])	创建一个复数
    # str(x )	将对象 x 转换为字符串
    # repr(x )	将对象 x 转换为表达式字符串
    # eval(str )	用来计算在字符串中的有效 Python 表达式,并返回一个对象
    # tuple(s )	将序列 s 转换为一个元组
    # list(s )	将序列 s 转换为一个列表
    # chr(x )	将一个整数转换为一个字符
    # unichr(x )	将一个整数转换为 Unicode 字符
    # ord(x )	将一个字符转换为它的整数值
    # hex(x )	将一个整数转换为一个十六进制字符串
    # oct(x )	将一个整数转换为一个八进制字符串

    # print(len([1, 2, 3]))
    # print([1, 2, 3] + [4, 5, 6])
    # print(['Hi'] * 4)
    # print(3 in [1, 2, 3])
    # for x in [1, 2, 3]:
    #     print(x)
    # list1 = ['两点水', 'twowter', 'liangdianshui', 123]
    # del(list1[0:2])
    # list1.append('hello')
    # print(list1)

    # cmp(list1, list2)
    # 比较两个列表的元素
    # len(list)
    # 列表元素个数
    # max(list)
    # 返回列表元素最大值
    # min(list)
    # 返回列表元素最小值
    # list(seq)
    # 将元组转换为列表
    # list.append(obj)
    # 在列表末尾添加新的对象
    # list.count(obj)
    # 统计某个元素在列表中出现的次数
    # list.extend(seq)
    # 在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
    # list.index(obj)
    # 从列表中找出某个值第一个匹配项的索引位置
    # list.insert(index, obj)
    # 将对象插入列表
    # list.pop(obj=list[-1])
    # 移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
    # list.reverse()
    # 反向列表中元素
    # list.sort([func])
    # 对原列表进行排序

    # tuple1 = ('两点水', 'twowter', 'liangdianshui', 123, 456)
    # tuple2 = '两点水', 'twowter', 'liangdianshui', 123, 456
    # # 创建空元组
    # tuple3 = ()
    # # 元组中只包含一个元素时，需要在元素后面添加逗号
    # tuple4 = (123,)
    # print(tuple1)
    # del(tuple1)
    # print(len((1, 2, 3)))
    # print((1, 2, 3) + (4, 5, 6))
    # print(('Hi') * 4)
    # print(3 in (1, 2, 3))
    # for x in (1 ,2, 3):
    #     print(x)

    # cmp(tuple1, tuple2)
    # 比较两个元组元素
    # len(tuple)
    # 计算元组元素个数
    # max(tuple)
    # 返回元组中元素最大值
    # min(tuple)
    # 返回元组中元素最小值
    # tuple(seq)
    # 将列表转换为元组

    dict1 = {'liangdianshui': '111111', 'twowater': '222222', '两点水': '333333'}
    # print(dict1)
    # 通过 key 值，删除对应的元素
    # del dict1['twowater']
    # print(dict1)
    # 删除字典中的所有元素
    # dict1.clear()
    # print(dict1)
    # 删除字典
    # del dict1
    # dict （字典）键必须不可变，可是键可以用数字，字符串或元组充当，但是就是不能使用列表
    # cmp(dict1, dict2)
    # 比较两个字典元素
    # len(dict)
    # 计算字典元素个数
    # str(dict)
    # 输出字典可打印的字符串表示
    # type(variable)
    # 返回输入的变量类型，如果变量是字典就返回字典类型
    # dict.clear()
    # 删除字典内所有元素
    # dict.copy()
    # 返回一个字典的浅复制
    # dict.values()
    # 以列表返回字典中的所有值
    # popitem()
    # 随机返回并删除字典中的一对键和值
    # dict.items()
    # 以列表返回可遍历的(键, 值)
    # 元组数组
    # print(dict1.values())
    # print(dict1.items())
    # print(str(dict1))

    # set1 = set([123, 456, 789, 123, 123])
    # set1.add(100)
    # set1.remove(123)
    # print(set1)

    # set1 = set('hello')
    # set2 = set(['p', 'y', 'y', 'h', 'o', 'n'])
    # print(set1)
    # print(set2)
    #
    # # 交集 (求两个 set 集合中相同的元素)
    # set3 = set1 & set2
    # print('\n交集 set3:')
    # print(set3)
    # # 并集 （合并两个 set 集合的元素并去除重复的值）
    # set4 = set1 | set2
    # print('\n并集 set4:')
    # print(set4)
    # # 差集
    # set5 = set1 - set2
    # set6 = set2 - set1
    # print('\n差集 set5:')
    # print(set5)
    # print('\n差集 set6:')
    # print(set6)

    # # 去除海量列表里重复元素，用 hash 来解决也行，只不过感觉在性能上不是很高，用 set 解决还是很不错的
    # list1 = [111, 222, 333, 444, 111, 222, 333, 444, 555, 666]
    # set7 = set(list1)
    # print('\n去除列表里重复元素 set7:')
    # print(set7)

    # count = 0
    # while count < 5:
    #     print(count)
    #     count = count + 1
    # else:
    #     print(count)

    # for num in range(10, 20):  # 迭代 10 到 20 之间的数字
    #     for i in range(2, num):  # 根据因子迭代
    #         if num % i == 0:  # 确定第一个因子
    #             j = num / i  # 计算第二个因子
    #             print('%d 是一个合数' % num)
    #             break  # 跳出当前循环
    #     else:  # 循环的 else 部分
    #         print('%d 是一个质数' % num)

    # 99乘法表
    for i in range(1, 10):
        for j in range(1, i + 1):
            print('{} x {} = {}\t'.format(i, j, i * j), end='')
        print()
    print('\n'.join([' '.join('%dx%d=%2d' % (x, y, x * y) for x in range(1, y + 1)) for y in range(1, 10)]))

    # 判断是否是闰年
    # year = int(input("请输入一个年份: "))
    # if (year % 4) == 0 and (year % 100) != 0 or (year % 400) == 0:
    #     print('{0} 是闰年'.format(year))
    # else:
    #     print('{0} 不是闰年'.format(year))

    # if not (isinstance(var_one, (int, float)) and isinstance(var_two, (int, float))):
    #     raise  TypeError('参数类型错误')
    # print(var_two + var_one)
    #
    # onetwo = var_one % var_two
    # twoone = (var_one - onetwo) / var_two
    # return onetwo, twoone


_no_value = object()


def print_info(a, b=_no_value):
    if b is _no_value:
        print('')


def print_info2(name, age, *hobby):
    # 打印用户信息
    print('昵称：{}'.format(name), end=' ')
    print('年龄：{}'.format(age), end=' ')
    print('爱好：{}'.format(hobby))
    return;


def print_info3(name, age, **hobby):
    # 打印用户信息
    print('昵称：{}'.format(name), end=' ')
    print('年龄：{}'.format(age), end=' ')
    print('爱好：{}'.format(hobby))
    return;


def print_info4(name, *, age, sex='男'):
    # 打印用户信息
    print('昵称：{}'.format(name), end=' ')
    print('年龄：{}'.format(age), end=' ')
    print('性别：{}'.format(sex))
    return;


# print_info2('Kinsgley', 18, '打篮球','打羽毛球','跑步')
# print_info3('Kinsgley', 18, hobby=('打篮球','打羽毛球','跑步'))
# print_info4(name = '两点水' ,age = 18 , sex = '女')


# sum = lambda num1, num2: num1 + num2
# print(sum(1, 2))

# # 1、字符创创建迭代器对象
# str1 = 'liangdianshui'
# iter1 = iter(str1)
#
# # 2、list对象创建迭代器
# list1 = [1, 2, 3, 4]
# iter2 = iter(list1)
#
# # 3、tuple(元祖) 对象创建迭代器
# tuple1 = (1, 2, 3, 4)
# iter3 = iter(tuple1)
#
# # for 循环遍历迭代器对象
# for x in iter1:
#     print(x, end=' ')
#
# print('\n------------------------')
#
# # next() 函数遍历迭代器
# while True:
#     try:
#         print(next(iter3))
#     except StopIteration:
#         break


# list1 = list(range(1, 11))
# print(list1)
# list2 = [x * x for x in range(1, 11)]
# print(list2)
# list3 = [x * x for x in range(1, 11) if x % 2 == 0]
# print(list3)
# list4 = [(x + 1, y + 1) for x in range(3) if x % 2 != 0 for y in range(5) if y % 2 != 0]
# print(list4)

# 生成器
# List 和 generator 的区别仅在于最外层的 [] 和 ()
# gen = (x * x for x in range(10))
# print(gen)

def my_function():
    for i in range(10):
        yield i


# print(my_function())

def fibon(n):
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, a + b


# 引用函数
# for x in fibon(1000000):
#     print(x , end = ' ')

def odd():
    print('step 1')
    yield (1)
    print('step 2')
    yield (3)
    print('step 3')
    yield (5)


# o = odd()
# print(next(o))
# print(next(o))
# print(next(o))

def triangles(n):  # 杨辉三角形
    L = [1]
    while True:
        yield L
        L.append(0)
        L = [L[i - 1] + L[i] for i in range(len(L))]


# n = 0
# for t in triangles(10):   # 直接修改函数名即可运行
#     print(t)
#     n = n + 1
#     if n == 10:
#         break

# list1 = [1,2,3,4,5]
# for num1 in reversed(list1):
#     print(num1, end=' ')

# names = ['laingdianshui', 'twowater', '两点水']
# ages = [18, 19, 20]
# dict1 = dict(zip(names, ages))
# print(dict1)
# list111 = list(range(12))
# print(list111)

# print(version)
# print(executable)

if __name__ == '__main__':
    print('yes')
else:
    print('no')
