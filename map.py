def func(x):
    return x ** 2


res_1 = map(len, ['hello', '123', 'python'])
res_2 = map(str.upper, ['hello', '123', 'python'])
res_3 = map(func, range(1, 5))
res_4 = map(lambda x: x ** 2, range(1, 5))
res_5 = map(lambda x, y: x + y, range(1, 5), range(5, 10))

print(res_1)
print(*res_1)
print(*res_2)
print(*res_3)
print(*res_4)
print(*res_5)