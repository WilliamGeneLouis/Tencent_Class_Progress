"""
Author: William
Date: 2022-01-15 18:55:25
LastEditTime: 2022-02-04 10:43:31
LastEditors: Please set LastEditors
Description: 打开GoroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: /undefined/Users/gustier.iu/Documents/课程学习进度/Untitled-1.py
"""

print("hello world")

print('whoami')

s = ' i love python'

print(s.split())  # 分割字符串

print('x'.join(['i', 'love', 'python']))  # 添加字符在固定的区间

print(('y'.join(s.split())))

print(s.strip())  # 去除句尾和句首的空格

print(s.index('o'))  # 输出该字符首次出现的位置

print(s.replace(' ', '#'))  # 用后边的字符代替文本中出现的所有需要替换的字符

print(s.find('i'))  # 与index用法类似

print(s.count('o'))  # 计算该字符在文本中出现的次数

print(s.endswith('on'))  # 布尔类型的判断句末是否一致

print(s.startswith(' '))  # 与end-with类似

a_list = ['physics', 'chemistry', 1997, 2000]

print(a_list.append('mango'))

print(a_list)  # 自动在列表末端添加一个字符串 append没有返回值

print(a_list.extend(['x', 'y']))

print(a_list)  # 自动在当前列表后扩展一个新的列表

print(a_list + ['x', 'y'])

print(a_list)

print(a_list.insert(2, 'z'))  # 在固定位置插入字符

print(a_list)

discard = a_list.pop()  # 将最后一个字符赋值给 discard 并且删除

print(discard)

print(a_list)

a_list.pop(0)  # 删除位于第一位置的字符  缺点： 耗时长

print(a_list)

print()

big_fruits = [list(a_list) for i in range(3)]  #

print(big_fruits)

# [i for i in range(10) if 1 % 2 == 0]     从一到十进行循环 范围： 0 - 10

b = (1,)

print(type(b))

# 向元组中添加元素

a_tuple = ('physics', 'chemistry', 1997, 2000, [])

a_tuple[-1].append('william')

print(a_tuple)

# 数据类型-sequence (string , list , tuple) & 控制流 for循环语句

a_string = 'abcdef'

a_list = list(a_string)

print(a_list)  # 输出中括号

a_tuple = tuple(a_list)

print(a_tuple)  # 输出小括号
print(' \n')

# 循环语句

# 输出字符串以及下标
for char in a_string:
    print(char, end='')
print(' \n')

for index, char in enumerate(a_string):
    print((index, char), end='')
print(' \n')

# 输出列表以及下标
for element in a_list:
    print(element, end='')
print(' \n')

for index, element in enumerate(a_list, 1):  # 此时1代表下标从1开始
    print((index, element), end='')
print(' \n')

# 输出元组以及下标
for element in a_tuple:
    print(element, end='')
print(' \n')

for index, element in enumerate(a_tuple, 11):  # 此时11代表下标从11 开始
    print((index, element), end='')
print(' \n')

# while循环语句

a_list = list('abcdefg')

index = 0
while index < len(a_list):
    print(a_list[index], '\t', end='')
    if a_list[index] == 'x':
        print("x found")
        break
    index += 1
else:
    print("x not found")

a_list = list('abxcdefg')

index = 0
while index < len(a_list):
    print(a_list[index], '\t', end='')
    if a_list[index] == 'x':
        print("x found")
        break
    index += 1
else:
    print("x not found")

print('\n')

# Python_basic_prac_01

# finished in GitHub

# 数据类型-dictionary

a_dict = {'abc': 123, 98.6: 37, (1, 2): 200}

print(a_dict)

del a_dict['abc']

print(a_dict)

print(a_dict.get(98.6))  # 查询字典中的数据并且返回value值

print(a_dict.get('abc'))  # 查询不到返回none

print(a_dict.get('abc', -1))  # 查询不到返回-1

print(a_dict.keys())

print(a_dict.values())

print(a_dict.items())

print(a_dict.pop(98.6))

print(a_dict)

a_dict_01 = {'x': 123, 'y': 1134}

a_dict.update(a_dict_01)

print(a_dict)

a_dict.clear()

print(a_dict)

# 数据类型-set

s = {2, 'x'}

print(2 in s)

print(4 in s)

s.add(4)

print(4 in s)

s.remove(4)

print(4 in s)

# 集合的运算

s1 = set(range(3))

s2 = set(range(2, 5))

print(s1, s2)

# 交集

print(s1 & s2)

# 并集

print(s1 | s2)

# 差集

print(s1 - s2)

# 对称集  cap 帽子符号

print(s1 ^ s2)  # 先并起来然后删除共有的部分


# 函数

def func(p):
    print("p is {}".format(p))


func(4)


def default(a, b=1, c=2):
    print('a is {}, b is {}, c is {}'.format(a, b, c))


default(1, 1, 1)
default(1, c=1)
default(1)


def change_func(a, *args, **kwargs):
    print('a is {}, args is {}, kwargs is {}'.format(a, args, kwargs))


change_func(1)
change_func(1, c=1)
change_func(1, 1, 1)
change_func(1, 1, 1, c=1)

args = (0, 10, 2)
print(list(range(*args)))

# 函数--作用域

total = 2


def sum(arg1, arg2):
    total = arg1 + arg2
    print('total value is {} in function'.format(total))
    return total


sum(10, 20)
print('total value is {} in here'.format(total))

# 面向函数编程

a = [0, 1, 2, 3, 4, 5]

filter_result = list(filter(lambda x: x % 2 == 0, a))

print(filter_result)

map_result = list(map(lambda x: x ** x, a))

print(map_result)

from functools import reduce

reduce_result = reduce(lambda a, b: a + b, a, 0)

print(reduce_result)

