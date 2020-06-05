# 使用zip同时遍历两个迭代器
names = ['sky', 'wangzitiansky', 'jjjjjddddwwwzztt', 'sssskkkkllll']
letters = [len(name) for name in names]
max_letters = 0
longest_name = None
for i, name in enumerate(names):
    count = letters[i]
    if count > max_letters:
        longest_name = name
        max_letters = count
print(longest_name)

for name, count in zip(names, letters):
    if count > max_letters:
        longest_name = name
        max_letters = count

'''
输出:
jjjjjddddwwwzztt
'''

from itertools import zip_longest


a = [1, 2, 3]
b = [1, 2, 3, 4, 5 ,6]

print(list(zip_longest(a, b)))

'''
输出
[(1, 1), (2, 2), (3, 3), (None, 4), (None, 5), (None, 6)]
'''

print(list(zip_longest(a, b, fillvalue='-')))

'''
输出:
[(1, 1), (2, 2), (3, 3), ('-', 4), ('-', 5), ('-', 6)]
'''