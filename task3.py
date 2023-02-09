s = input().split()
print(
      all(
          map(
              lambda x: x == x[::-1],
              filter(str.isalpha, s)
          )
      )
)