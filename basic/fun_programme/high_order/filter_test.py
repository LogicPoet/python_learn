# 过滤偶数，保留奇数
def is_odd(n):
    return n % 2 == 1


# 过滤掉空字符串《return的是规则，符合条件不被过滤的规则,true:符合，false:不符合》
def not_empty(s):
    return s and s.strip()


# 埃式筛法，求素数
def _not_divisible(n):
    return lambda x: x % n > 0


#  过滤出回数 ??
def is_palindrome(n):
    return str(n) == str(n)[::-1]


# filter 过滤《第一个是过滤的规则函数》
result = list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))
print(result)

result = list(filter(not_empty, ['A', '', 'B', None, 'C', '  ']))
print(result)

output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101,
                                                  111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')
