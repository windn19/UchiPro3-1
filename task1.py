words = input().split()
print(
    *sorted(
        words,
        key=lambda s: (len(s), s)
    )
)