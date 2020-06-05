# 用列表推导式取代map filter
# 列表推导式
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = [x**2 for x in a]
print(squares)
'''
输出
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
'''

# 列表推导式
even_squares = [x ** 2 for x in a if x % 2 == 0]
print(even_squares)
'''
输出
[4, 16, 36, 64, 100]
'''

# 如果用map + filter来做
alt = map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, a))
print(list(alt))
'''
输出
[4, 16, 36, 64, 100]
'''

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
