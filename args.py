def average(*args, **kwargs):
    print(args)
    print(kwargs)
    result = sum(args) / len(args)
    if 'precision' in kwargs:
        return round(result, kwargs['precision'])
    return round(result)


print(average(2, 3))
print(average(2, 3, 3))
print(average(2, 3, 3, precision=3))
print(average(2, 3, 3, 5, precision=3, test='test'))
