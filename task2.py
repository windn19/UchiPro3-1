s = input().split()
print(
      max(
          filter(
                 str.isdigit,
                 s),
          key=lambda n: sum(
                            map(
                                int,
                                list(n)
                               )
                           )
         )
     )