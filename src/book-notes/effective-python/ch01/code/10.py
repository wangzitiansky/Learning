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

# 也可以用来生成包含元组的列表
enumerate_list = list(enumerate(flavor_list))
print(enumerate_list)

'''
输出:
[(0, 'vanilla'), (1, 'chocolate'), (2, 'pecan'), (3, 'strawberry')]
'''