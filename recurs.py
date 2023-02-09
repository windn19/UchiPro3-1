def rec_for(n):
    print(n)
    total = 1
    for i in range(1, n + 1):
        total *= i
    return total


def rec_fact(n):
    print(n)
    if n == 0:
        return 1
    return n * rec_fact(n - 1)


n = 10
print(rec_for(n))
print(rec_fact(n))
