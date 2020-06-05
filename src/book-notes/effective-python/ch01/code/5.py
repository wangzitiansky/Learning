# 了解切割序列的方法
a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print('First Four:', a[:4])
print('Last Four:', a[-4:])
print('middle two', a[3:-3])

# 切片是浅拷贝
a = [[1, 2, 3], [1, 2, 3]]
b = a[:]
print(b)
a[0][0] = -1
print(b)