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

