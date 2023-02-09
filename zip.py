res1 = zip([1, 2, 3], 'abc')
res2 = zip([1, 2, 3], 'abc', '#$')
res3 = zip(range(5), 'hello')

print(res1)
# print(*res1)
print(dict(res1))
print(*res2)
print(*res3)
