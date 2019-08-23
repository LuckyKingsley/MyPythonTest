#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2019/4/24 15:43
#@Author: Kingsley
#@File  : test190424.py

# age = None
# if age:
#     print('your age is', age)
#     print('adult')
# else:
#     print("no")

# age = input('birth:')
# birth = int(age)
# print(birth)

# 小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：
#
# 低于18.5：过轻
# 18.5-25：正常
# 25-28：过重
# 28-32：肥胖
# 高于32：严重肥胖
# bmi = math.pow(80.5/1.75, 4)
# if bmi < 18.5:
#     print('过轻')
# elif bmi >=18.5 or bmi < 25 :
#     print('正常')
# else:
#     print('lese')

# names = ['Michael', 'Bob', 'Tracy']
# for n in names:
#     print(n)

# sum = 0
# for x in range(50):
#     sum += x
# print(sum)

# a = list(range(100))
# for n in a:
#     print(n)

# sum = 0
# # n = 99
# # while n > 0:
# #     sum += n
# #     n = n - 1
# # print(sum)

# L = ['Bart', 'Lisa', 'Adam']
# for n in L:
#     print('hello', n)

# n = 1
# while n <= 100:
#     n += 1
#     if n % 2 == 0: # 当n = 11时，条件满足，执行break语句
#         continue # break语句会结束当前循环
#     print(n)
# print('END')

# n = 0
# while n < 10:
#     n = n + 1
#     if n % 2 == 0: # 如果n是偶数，执行continue语句
#         continue # continue语句会直接继续下一轮循环，后续的print()语句不会执行
#     print(n)

# d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
# print(d['Bob'])
# d['Admin']=60
# print(d['Admin'])
# print('Thomas' in d)
# print(d.get('Thomas', -1))
# d[(1,2,3)] = 123
# print(d)


# s1 = set([1, 2, 3])
# s2 = set([2, 3, 4])
# print(s1 & s2)
# print(s1 | s2)

# s1 = set(1, 2, 3)
# s2 = set(2, 3, 4)
# print(s1 & s2)
# print(s1 | s2)

# a, b, c, d = 20, 5.5, True, 4+3j
# print(type(a), type(b), type(c), type(d))
# print(2//4)
# print(2/4)
# print(2**200000)

# str = 'Runoob'
# print(str)  # 输出字符串
# print(str[0:-1])  # 输出第一个到倒数第二个的所有字符
# print(str[0])  # 输出字符串第一个字符
# print(str[2:5])  # 输出从第三个开始到第五个的字符
# print(str[2:])  # 输出从第三个开始的后的所有字符
# print(str * 2)  # 输出字符串两次
# print(str + "TEST")  # 连接字符串

# print('Ru\noob')
# print(r'Ru\noob')

# student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}
# print(student)  # 输出集合，重复的元素被自动去掉
# # 成员测试
# if 'Rose' in student:
#     print('Rose 在集合中')
# else:
#     print('Rose 不在集合中')
# # set可以进行集合运算
# a = set('abracadabra')
# b = set('alacazam')
# print(a)
# print(a - b)  # a 和 b 的差集
# print(a | b)  # a 和 b 的并集
# print(a & b)  # a 和 b 的交集
# print(a ^ b)  # a 和 b 中不同时存在的元素

# dict = {}
# dict['one'] = "1 - 菜鸟教程"
# dict[2] = "2 - 菜鸟工具"
# tinydict = {'name': 'runoob', 'code': 1, 'site': 'www.runoob.com'}
# print(dict['one'])  # 输出键为 'one' 的值
# print(dict[2])  # 输出键为 2 的值
# print(tinydict)  # 输出完整的字典
# print(tinydict.keys())  # 输出所有键
# print(tinydict.values())  # 输出所有值

# dic = dict([('Runoob', 1), ('Google', 2), ('Taobao', 3)])
# print(dic)
# dic = dict(Runoob=1, Google=2, Taobao=3)
# print(dic)
# dic = {x: x ** 2 for x in (2, 4, 6)}
# print(dic)
# dic = {'Runoob': 1, 'Google': 2, 'Taobao': 3}
# print(dic)
# dic = {2: 4, 4: 16, 6: 36}
# print(dic)

# a = ['c', 'b', 'a']
# a.sort()
# print(a)

# a = 'abc'
# b = a.replace('a', 'A')
# print(b)

# r1 = 12.34
# r2 = 9.08
# r3 = 73.1
# s1 = 3.14 * r1**2
# s2 = 3.14 * r2**2
# s3 = 3.14 * r3**2
# print(s1,s2,s3)

# print(abs(100))
# print(abs(-20))
# print(abs(12.23))
# print(max(1,2,3,-1,0,-3))
# print(int('12'))
# print(bool(1))

# a = abs()
# print(a(-121))

# a=123
# print(hex(a))


# from collections import Iterable


# print(my_abs(-3))
# print(nop())
# print(testInstance(True))

# x, y = move(100, 100, 60, math.pi / 6)
# print(x, y)
# r = move(100, 100, 60, math.pi / 6)
# print(r)

# r = quadratic(2, 3, 1)
# print(r)
# r = math.sqrt(2)
# print(r)

# print(odsad(3))

# L = []
# print(add_end(L))

# print(calc(*(1, 3, 5)))
# print(calc(1, 3, 5))

# person('Michael', 30)
# person('Bob', 35, city = 'Beijing', job = 'Engineer')

# person2('Jack', 24, city='Beijing', addr='Chaoyang', zipcode=123456)
# person2('Jack', 24, city='Beijing', addr='Chaoyang', zipcode=123456)
# person3('Jack', 24, city='Beijing', job='Engineer')
# person3('Jack', 24, city='Beijing', job='Engineer')
# person4('Jack', 24, [1,2], city='Beijing', job='Engineer')
# person5('Jack', 24, job='Engineer')

# f1(1,2)
# f1(1,2,c=3)
# f1(1,2,3,'a','b')
# f1(1,2,3,'a','b', x=99)
# f1(1,2,3,'a','b',{'x':99,'job':'Engineer'},x=99,job='Engineer')
# f2(1,2,d=99,x=99,job='Engineer')
# args = (1,2,3,4)
# kw = {'d':99, 'x':'#'}
# f1(*args, **kw)
# args = (1, 2, 3)
# kw = {'d': 88, 'x': '#'}
# f2(*args,**kw)

# product(1,2,3,4)

# print(fact(100))
# move(4, 'A', 'B', 'C')

# L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
# print(L[0:3])
# print(L[:3])
# print(L[-2:])

# L = list(range(100))
# print(L)
# print(L[:10])
# print(L[:10:2])
# print(L[:10])
# M = tuple(range(100))
# print(M[:10])
# i = '   F UISP  CWI   '
# print(i[1:3])

# print(trim(i))
# print(trim2(i))

# print(isinstance('abc', Iterable)) # str是否可迭代
# print(isinstance([1,2,3], Iterable)) # list是否可迭代
# print(isinstance(123, Iterable))
# for i, value in enumerate(['A', 'B', 'C']):
#     print(i, value)
# print(findMinAndMax([1, 3, 6, 0, -3]))

# print([x * x for x in range(1, 11) if x % 2 == 0])
# print([m + n for m in 'ABC' for n in 'XYZ'])
# print([d for d in os.listdir('.')])

# d = {'x': 'A', 'y': 'B', 'z': 'C' }
# for k, v in d.items():
#     print(k, '=', v)
# L = ['hello', 'world', 'ibm', 'apple']
# print([s.upper() for s in L])
# L1 = ['Hello', 'World', 18, 'Apple', None]
# L2 = []
# for n in L1:
#     # if not isinstance(n, str):
#     #     L1.remove(n)
#     # else:
#     #     pass
# # print(L1)
#     if not isinstance(n, str):
#         pass
#     else:
#         L2.append(n)
# print(L2)

# L = [x * x for x in range(10)]
# print(L)
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# g = (x * x for x in range(2))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))

# print(fib(100))
# o = odd()
# print(next(o))
# print(next(o))
# print(next(o))
# print(next(o))
# while True:
#     try:
#         print(next(o))
#     except StopIteration as e:
#         print('Generator return value:', e.value)
#         break

# triangles(6)

# print(list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])))

# print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))

# print(_odd_iter().__next__())
# print(_odd_iter().__next__())
# print(_odd_iter().__next__())
# print(_odd_iter().__next__())
# print(_odd_iter().__next__())

# print(sorted([36, 5, -12, 9, -21], key= abs))
# print(sorted(['bob', 'about', 'Zoo', 'Credit']))
# print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))
# print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse= True))

# L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# print(sort_by_name(L))
# print(by_score(L))

# print(lazy_sum(1,3,4,5)())

# f1 = count()
# print(f1[0]())
# print(f1[1]())
# print(f1[2]())
# print(f2())
# print(f3())
# print(f4())

# print(createCounter())
# print(createCounter())
# print(createCounter())
# print(createCounter())
# print(createCounter())
# print(createCounter())

# print(list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])))

