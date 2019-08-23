# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2019/4/26 9:43
# @Author: Kingsley
# @File  : test190426.py

import math

def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x

def nop():
    pass

def testInstance(x):
    if not isinstance(x, (int, float, bool)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

def quadratic(a, b, c):
    if a == 0:
        raise TypeError('a不能为0')
    if a == 0 and b == 0 and c == 0:
        raise TypeError('三个参数不能都为0')

    if not isinstance(a, (int, float)) \
            or not isinstance(b, (int, float)) \
            or not isinstance(c, (int, float)):
        raise TypeError('参数类型传错')

    delta = b**2 - 4 * a * c
    if delta < 0:
        return '无实根'
    else:
        x1 = (math.sqrt(delta) - b) / (2 * a)
        x2 = -(math.sqrt(delta) + b) / (2 * a)
        return x1, x2

def odsad(x, n = 2):
    return x**n

def add_end(L = None):
    if L is None:
        L = []
    L.append('END')
    return L

def calc(*numbers):
    sum = 0
    for n in numbers:
        sum += n**2
    return sum


def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)
def person2(name, age, **kw):
    if 'city' in kw:
        pass
    elif 'job' in kw:
        pass
    else:
        print('name:', name, 'age:', age, 'other:', kw)
def person3(name, age, *, city, job):
    print(name, age, city, job)
def person4(name, age, *args, city, job):
    print(name, age, args, city, job)
def person5(name, age, *, city='Beijing', job):
    print(name, age, city, job)

def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)
def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

def product(*args):
    x = 1
    for n in args:
        print(n)
        x = x * n
        print(x)

def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)

def move(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
    else:
        move(n - 1, a, c, b)
        print(a, '-->', c)
        move(n - 1, b, a, c)

def trim(s):
    return s.replace(' ', '')
def trim2(s):
    a = s.split()
    b = ''.join(a)
    return b

def findMinAndMax(L):
    if not isinstance(L, list):
        raise TypeError('INVALID')

    L_num = [x for x in L if type(x) is int]
    if len(L_num) == 0:
        return (None, None)
    else:
        min = 0
        max = 0
        for i, value in enumerate(L_num):
            if i == 0:
                min = value
                max = value
            else:
                if value > max:
                    max = value
                elif (value < min):
                    min = value
                else:
                    pass
        return (min, max)

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'

def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield(3)
    print('step 3')
    yield(5)
    return 'done'

def triangles(num):
    print([1])
    line = [1, 1]
    print(line)

    for i in range(2, num):
        r = []
        for i in range(0, len(line) - 1):
            r.append(line[i] + line[i+1])
        line = [1] + r + [1]
        print(line)

def is_odd(n):
    return n % 2 == 1

def not_empty(s):
    return s and s.strip()

def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n


def sort_by_name(t):
    if not isinstance(t, (tuple, list)):
        raise TypeError("传入参类型不符")
    else:
        t2 = []
        t3 = dict(t)
        for n in t3.keys():
            t2.append(n)
        t4 = sorted(t2)
        t5 = []
        for n in t4:
            t5.append((n, t3[n]))

        return t5

def by_score(t):
    if not isinstance(t, (tuple, list)):
        raise TypeError("传入参类型不符")
    else:
        t2 = []
        t3 = dict(t)
        for n in t3.values():
            t2.append(n)
        t4 = sorted(t2, key= abs, reverse= True)
        t5 = []
        for n in t4:
            for k, v in t3.items():
                if v == n:
                    m = k
                    t5.append((m, n))
                else:
                    pass

        return t5

def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

def count():
    def f(j):
        def g():
            return j * j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i))
    return fs

s = 0
def createCounter():
    def counter(s):
        def counterInner():
            global s
            s += 1
            return s
        return counterInner()
    return counter(s)




