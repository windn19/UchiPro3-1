def power(n, k):
    if k == 0:
        return 1
    return n * power(n, k - 1)


n, k = map(int, input().split())
print(power(n, k))
