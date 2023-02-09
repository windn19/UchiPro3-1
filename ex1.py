lst = [(5, 6), (121, 10), (20, 1, 1), (1, 2, 1)]
print(
    *filter(
            lambda s: s == s[::-1],
            map(lambda x: str(sum(x)),
                lst)
            )
)
