def average(a, b, c, precision=0):
    result = (a + b + c) / 3
    return round(result, precision)


print(average(a=2, c=3,  b=3, precision=3))
print(average(2, 3, 3, 1))
print(average(2, 3, 3))
