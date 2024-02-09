text = ['Явное\n', 'лучше,\n', 'чем\n', 'неявное\n']

with open('output.txt', 'w', encoding='utf-8') as file:
    file.writelines(text)
