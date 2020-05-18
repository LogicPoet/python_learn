# sorted()也是一个高阶函数。用sorted()排序的关键在于实现一个映射函数。

# 内置sorted排序<数学上的排序(只能是数值)>
result = sorted([35, 11, -13, 9, 0, 11, 11.2])
print(result)

# 自定义排序(可以接受key函数，改变排序规则)
# key指定的函数将作用于list的每一个元素上，并根据key函数返回的结果进行排序
# 然后sorted()函数按照keys进行排序，并按照对应关系返回list相应的元素
result = sorted([35, 11, -13, 9, 0, 11, 11.2], key=abs)
print(result)

# 默认是按照ASCII的大小排序<从前往后>
result = sorted(['bob', 'about', 'Zoo', 'Credit'])
print(result)

# 通过key函数，忽略大小写
result = sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower)
print(result)

# 可以选择正序或者反序reverse参数,True从大到小，false从小到大，默认是false，
result = sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)
print(result)

# 练习
# 假设我们用一组tuple表示学生名字和成绩：
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


# 请用sorted()对上述列表分别按名字排序：
def by_score(n):
    # n[0] 按名字排序，n[1]按分数排序
    return n[1]


L2 = sorted(L, key=by_score)
print(L2)
