#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2019/8/23 15:03
# @Author: Kingsley
# @File  : test19082311.py


# 正则表达式
import re

####################################1111111111111111111
# 设定一个常量
a = '两点水|twowater|liangdianshui|草根程序员|ReadingWithU'

# 判断是否有 “两点水” 这个字符串，使用 PY 自带函数

print('是否含有“两点水”这个字符串：{0}'.format(a.index('两点水') > -1))
print('是否含有“两点水”这个字符串：{0}'.format('两点水' in a))

findall = re.findall('两点水', a)
print(findall)
if len(findall) > 0:
    print('a 含有“两点水”这个字符串')
else:
    print('a 不含有“两点水”这个字符串')

# 选择 a 里面的所有小写英文字母
re_findall = re.findall('[a-z]', a)
print(re_findall)

#################################222222222222222222222222
print()
a = 'uav,ubv,ucv,uwv,uzv,ucv,uov'

# 字符集

# 取 u 和 v 中间是 a 或 b 或 c 的字符
findall = re.findall('u[abc]v', a)
print(findall)
# 如果是连续的字母，数字可以使用 - 来代替
l = re.findall('u[a-c]v', a)
print(l)

# 取 u 和 v 中间不是 a 或 b 或 c 的字符
re_findall = re.findall('u[^abc]v', a)
print(re_findall)
re_l = re.findall('u[^a-c]v', a)
print(re_l)

#####################################33333333333333333333333333
print()
a = 'uav_ubv_ucv_uwv_uzv_ucv_uov&123-456-789'
# \d 相当于 [0-9] ,匹配所有数字字符
# \D 相当于 [^0-9] ， 匹配所有非数字字符
findall1 = re.findall('\d', a)
findall2 = re.findall('[0-9]', a)
findall3 = re.findall('\D', a)
findall4 = re.findall('[^0-9]', a)
print(findall1)
print(findall2)
print(findall3)
print(findall4)

# \w 匹配包括下划线的任何单词字符，等价于 [A-Za-z0-9_]
findall5 = re.findall('\w', a)
findall6 = re.findall('[A-Za-z0-9_]', a)
findall7 = re.findall('[^A-Za-z0-9_]', a)
print(findall5)
print(findall6)
print(findall7)

#######################################4444444444444444444444444444
a = 'java*&39android##@@python'

# 数量词
# 贪婪模式：它的特性是一次性地读入整个字符串，如果不匹配就吐掉最右边的一个字符再匹配，直到找到匹配的字符串或字符串的长度为 0 为止。它的宗旨是读尽可能多的字符，所以当读到第一个匹配时就立刻返回。
findall8 = re.findall('[a-z]{4,7}', a)
# 懒惰模式：它的特性是从字符串的左边开始，试图不读入字符串中的字符进行匹配，失败，则多读一个字符，再匹配，如此循环，当找到一个匹配时会返回该匹配的字符串，然后再次进行匹配直到字符串结束。
findall9 = re.findall('[a-z]{4,7}?', a)
print(findall8)
print(findall9)

# ?：告诉引擎匹配前导字符 0 次或 1 次
# +：告诉引擎匹配前导字符 1 次或多次
# *：告诉引擎匹配前导字符 0 次或多次
# ？	 ？？ 零次或一次出现，等价于{0,1}
# +	 +？	一次或多次出现 ，等价于{1,}
# *	 *？	零次或多次出现 ，等价于{0,}
# {n} {n}？	恰好 n 次出现
# {n,m}	{n,m}？	至少 n 次枝多 m 次出现
# {n,} {n,}？	至少 n 次出现

# ^	匹配字符串开头（在有多行的情况中匹配每行的开头）
# $	匹配字符串的末尾(在有多行的情况中匹配每行的末尾)
# \A	仅匹配字符串开头
# \Z	仅匹配字符串末尾
# \b	匹配 \w 和 \W 之间
# \B	\b


#######################################55555555555555555555555
# 替换字符串中的字符
a = 'Python*Android*Java-888'

# 把字符串中的 * 字符替换成 & 字符
sub1 = re.sub('\*', '&', a)
print(sub1)
# 把字符串中的第一个 * 字符替换成 & 字符
sub2 = re.sub('\*', '&', a, 1)
print(sub2)


# 把字符串中的 * 字符替换成 & 字符,把字符 - 换成 |
# 1、先定义一个函数
def convert(value):
    group = value.group()
    if (group == '*'):
        return '&'
    elif (group == '-'):
        return '|'


sub3 = re.sub('[\*-]', convert, a)
print(sub3)

###########################################666666666666666666666666666
print()
# re.match 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match() 就返回 none
# re.search 扫描整个字符串并返回第一个成功的匹配
# re.match 只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回 None；
# 而 re.search 匹配整个字符串，直到找到一个匹配。这就是它们之间的区别了。
a = '<img src="https://s-media-cache-ak0.pinimg.com/originals/a8/c4/9e/a8c49ef606e0e1f3ee39a7b219b5c05e.jpg">'

# 使用 re.search
search = re.search('<img src="(.*)">', a)
# group(0) 是一个完整的分组
print(search.group())
print(search.group(0))
print(search.group(1))

# 使用 re.findall
findall = re.findall('<img src="(.*)">', a)
print(findall)

# 多个分组的使用（比如我们需要提取 img 字段和图片地址字段）
re_search = re.search('<(.*) src="(.*)">', a)
# 打印 img
print(re_search.group(1))
# 打印图片地址
print(re_search.group(2))
# 打印 img 和图片地址，以元祖的形式
print(re_search.group(1, 2))
# 或者使用 groups
print(re_search.groups())
