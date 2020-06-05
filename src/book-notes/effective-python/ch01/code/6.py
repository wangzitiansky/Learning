# 切片操作不要同时指定start, end和stride
a = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
odds = a[::2]
evens = a[1::2]
print(odds)
print(evens)
'''
输出
['red', 'yellow', 'blue']
['orange', 'green', 'purple']
'''