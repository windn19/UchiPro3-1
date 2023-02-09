res_1 = filter(str.isalpha, ['hello', '123', 'python'])
res_2 = filter(lambda x: x % 2 == 0, range(1, 5))
res_3 = filter(lambda x: x < 10, [10, 4, 2, -1, 6])
res_4 = filter(lambda x: x > 10,
               map(lambda x, y: x + y,
                   range(1, 5), range(5, 10))
               )
print(res_1)
print(*res_1)
print(*res_2)
print(*res_3)
print(*res_4)