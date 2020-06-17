# 用Pythonic的方式来思考

| 标题                        | 链接                            | 备注                              |  打卡日期 :date:  |
|-----------------------------|---------------------------------|----------------------------------|-------------|
|确认自己的python版本          |[第一条](#第一条)                 |                     |  |
|了解切割序列的方法            | [第五条](#第五条)                |    切片操作介绍        | |
|切片不要同时指定start, end, strde|[第六条](#第六条)              |    切片操作规范         | |
|用列表推导式取代map,filter    |[第七条](#第七条)                 |    尽量使用列表推导式   | |
|不要使用含两个以上表达式的列表推导|[第八条](#第八条)             |    列表推导式中表达式数量不应过多| 2020.6.2 :crescent_moon: |
|用生成器表达式来改写数据量较大的列表推导|[第九条](#第九条)        | 使用生成器表达式来节省内存 | 2020.6.3 :sun_with_face: |
|使用enumerate取代range| [第十条](#第十条)   | enumerate的使用 | 2020.6.3 :sun_with_face: |
|用zip函数同时遍历两个迭代器|[第十一条](#第十一条)| 使用zip来遍历 | 2020.6.4 :sun_with_face:|
|不要再for和while循环后面写else块|[第十二条](#第十二条)|  杜绝这种奇怪的写法    | 2020.6.5 :bug:   |
| 合理利用try/except/else/finally|[第十三条](#第十三条)| 异常语句块的执行|    2020.6.5 :new:|
 
读书笔记 :school_satchel:

:rocket: 代码和大部分内容来自[Effective Python](https://book.douban.com/subject/26709315/) :clap: :clap: :clap:

## 第一条
确认自己所用的python版本

## 第二条
遵循PEP8风格

## 第三条
了解bytes str unicode的区别

### 要点

### 代码

## 第五条
了解切割序列的方法
### 要点

+ 当start索引为0或者end索引为序列长度时，应该省略

+ 切片操作不计较start或者end是否越界

+ 对list赋值时，如果使用切片操作，就会把原列表中处在相关范围内的值替换成新值，即使长度不同仍然可以替换

### 代码

切割序列的方法

```python
a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print('First Four:', a[:4])
print('Last Four:', a[-4:])
print('middle two', a[3:-3])
'''
输出
First Four: ['a', 'b', 'c', 'd']
Last Four: ['e', 'f', 'g', 'h']
middle two ['d', 'e']
'''
```

使用切片操作赋值是浅拷贝

```python
a = [[1, 2, 3], [1, 2, 3]]
b = a[:]
print(b)
a[0][0] = -1
print(b)
'''
输出
[[1, 2, 3], [1, 2, 3]]
[[-1, 2, 3], [1, 2, 3]]
可以看出对a的操作 影响了b 说明a[0] b[0]指向同一个list对象
'''
```

## 第六条

单次切片操作，不要同时指定start, end, strde

### 要点

+ 既有start和end和stride的切割操作，可能让人费解

+ 尽量使用stride为正数，而且不带start, end的切割操作，避免使用负数stride

+ 同一个切片操作，不要同时指定start, end, strde。如果确实需要执行这种操作，那就考虑两条赋值语句，一条做范围切割，另一条做补进切割

### 代码

```python
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
```

## 第七条

用列表推导式取代map和filter

### 要点

+ 列表推导式更清晰，因为不需要编写lambda函数

+ 列表推导式也可以达到map + filter的效果

+ 字典与集合也支持列表推导式

### 代码

列表推导式

```python
# 列表推导式
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = [x**2 for x in a]
print(squares)
'''
输出
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
'''
```

取代map + filter

```python
# 如果用map + filter来做
alt = map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, a))
print(list(alt))
'''
输出
[4, 16, 36, 64, 100]
'''

even_squares = [x ** 2 for x in a if x % 2 == 0]
print(even_squares)
'''
输出
[4, 16, 36, 64, 100]
'''
```

字典与集合的推导式

```python
# 字典与集合的推导式

source = {'ghost': 1, 'habanero': 2, 'cayenne': 3, 'caynnnn': 4}
target_dict = { value: name for name, value in source.items() }
len_set = { len(name) for name in source.keys() }
print(target_dict)
print(len_set)
'''
输出
{1: 'ghost', 2: 'habanero', 3: 'cayenne', 4: 'caynnnn'}
{8, 5, 7}
'''
```

## 第八条
不要使用含有两个表达式以上的列表推导

### 要点

+ 列表推导支持多重循环，没重循环也支持多项条件

+ 超过两个表达式的列表推导式是很难理解的，需要尽量避免

### 代码

列表推导式支持多重循环

```python
# 将二维矩阵展开为一维矩阵
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [x for row in matrix for x in row]
print(flat)
'''
输出:
[1, 2, 3, 4, 5, 6, 7, 8, 9]
'''

# 对二维矩阵的每个值 取平方
squared = [[x ** 2 for x in row] for row in matrix]
print(squared)
'''
输出:
[[1, 4, 9], [16, 25, 36], [49, 64, 81]]
'''
```

每重循环也支持多个条件

```python
# 列表推导式中有多个条件的情况
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = [x for x in a if x > 4 if x % 2 == 0]
c = [x for x in a if x > 4 and x % 2 == 0]
print(b)
print(c)
'''
输出:
[6, 8, 10]
[6, 8, 10]
'''

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
filtered = [
    [x for x in row if x % 3 == 0]
    for row in matrix if sum(row) >= 10
]
print(filtered)
'''
输出:
[[6], [9]]
'''
```

很多列表推导式难以阅读，应用其他方式替代

```python
# 列表推导式较长的情况
my_lists = [
    [[1, 2, 3], [4, 5, 6]]
]

flat = [x for sublist1 in my_lists for sublist2 in sublist1 for x in sublist2]
print(flat)
'''
输出：
[1, 2, 3, 4, 5, 6]
'''

# 应用for循坏代替
flat = []
for sublist1 in my_lists:
    for sublist2 in sublist1:
        flat.extend(sublist2)
print(flat)
'''
输出：
[1, 2, 3, 4, 5, 6]
'''
```

## 第九条
用生成器表达式来改写数据量较大的列表推导

### 要点

+ 当输入数据量较大时，列表推导过于占用内存

+ 生成器表达式所返回的迭代器，可以逐次产生输出值，从而避免内存问题

+ 生成器表达式可以组合

+ 串在一起的生成器表达式执行速度很快

### 代码

将列表推导改为生成器表达式

```python
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
```

某个生成器表达式所返回的迭代器，放在另一个生成器表达式的for子表达式中，二者可以组合起来

```python
roots = ((x, x ** 0.5) for x in it)
print(next(roots))
'''
输出
(13, 3.605551275463989)
'''
```

:date:6.3 打卡
:sunny:

## 第十条
尽量使用enumerate取代range

### 要点

+ enumerate函数提供一种精简的写法，可以在遍历迭代器的时候获知每个元素的索引

+ 尽量使用enumerate来改写那种将range和下标访问结合的序列遍历代码

+ enumerate提供第二个参数来指定开始计数时候所用的值

### 代码

enumerate的使用

```python
# 用enumerate取代range

flavor_list = ['vanilla', 'chocolate', 'pecan', 'strawberry']

for i in range(len(flavor_list)):
    flavor = flavor_list[i]
    print('%d %s' % (i + 1, flavor))

for i, flavor in enumerate(flavor_list, 1):
    print('%d %s' % (i, flavor))

'''
输出均是:
1 vanilla
2 chocolate
3 pecan
4 strawberry
'''
```

使用enumerate生成列表

```python
# 也可以用来生成包含元组的列表
enumerate_list = list(enumerate(flavor_list))
print(enumerate_list)

'''
输出:
[(0, 'vanilla'), (1, 'chocolate'), (2, 'pecan'), (3, 'strawberry')]
'''
```

:new:6.4打卡
:sunny:

## 第十一条
用zip函数同时遍历两个迭代器

### 要点

+ 内置的zip可以平行的遍历多个容器

+ Python3中zip相当于生成器，会在遍历的时候逐次生成元组，而Python2中的zip则是直接把这些元组完全生成好，并一次返回整份列表

+ 如果提供的迭代器长度不等，那么zip会提前终止

+ itertoos内置模块中的zip_longest函数可以平行的遍历多个迭代器而不用在乎它们的长度是否相等

### 代码

使用zip来迭代
```python
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
```

zip_longest的用法
```python
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
```

:date::new:2020.6.5

## 第十二条
不要再for和while循环后面写else

### 要点

+ Python有中特殊语法，可以再循环后面写一个else语句块

+ 只有当整个主题都没有break的时候，循环后面的else才执行

+ 不要在循环后面写else块，不直观，且容易被误解


## 第十三条
合理利用try/except/else/finally

### 要点

+ finally总是会执行

+ else在没有发生异常的时候执行

+ 在没有发生异常的时候，要在finally之前执行的语句，写入else块