from functools import reduce


res1 = reduce(lambda x, y: x + y, range(1, 5))
res2 = reduce(lambda x, y: x + y, range(1, 5), 10)
res3 = reduce(lambda x, y: [y] + x, [1, 2, 3, 4, 5], [])

print(res1)
print(res2)
print(res3)
