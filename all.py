print(all([]))

res1 = all([1, 2, 3, 1, 1])
res2 = all(map(str.isalpha, ['hello', '123', 'python']))
res3 = all(
            map(
                lambda x: x % 2 == 0,
                [1, 2, 3, 4, 5]
            )
          )
res4 = any(map(lambda x: x % 2 == 0, [1, 2, 3, 4, 5]))

print(res1)
print(res2)
print(res3)
print(res4)

