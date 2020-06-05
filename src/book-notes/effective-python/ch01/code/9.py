# 生成器表达式改写数据量较大的列表推导

value = [len(x) for x in open('d:/learn/learn_python/effective_python/ch01/code/my_txt.txt')]
print(value)
'''
输出
[7, 19, 13, 4, 20, 20, 13, 4, 2]
'''

it = (len(x) for x in open('d:/learn/learn_python/effective_python/ch01/code/my_txt.txt'))
print(it)
'''
输出:
<generator object <genexpr> at 0x0000018F12491820>
'''

print(next(it))
print(next(it))
'''
输出:
7
19
'''

roots = ((x, x ** 0.5) for x in it)
print(next(roots))
'''
输出
(13, 3.605551275463989)
'''