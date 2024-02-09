text1 = 'Явное лучше, чем неявное. \n'
text2 = 'Простое лучше, чем сложное. \n'
text3 = 'Сложное лучше, чем запутанное. \n'

with open('output.txt', 'w', encoding='utf-8') as file:
    print(text1, text2, text3, end='!!!', file=file)
    # file.write(text1)
    # file.write(text2)
    # file.write(text3)
