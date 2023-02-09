lst = []
for i in range(10, 20):
    if i % 2 == 0:
        lst.append(i ** 2)
print(lst)

lst = [i ** 2 for i in range(10, 20) if i % 2 == 0]
print(lst)

lst = list(map(lambda x: x ** 2,
               filter(lambda x: x % 2 == 0,
                      range(10, 20)
                      )
               )
           )
print(lst)