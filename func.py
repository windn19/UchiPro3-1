def add_one(a):
    return a + 1


f = add_one
print(type(f))
print(f(5))

add_one = lambda x: x + 1
print(type(add_one))
print(add_one(5))