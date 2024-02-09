file = open(file='text.txt', mode='r', encoding='utf-8')
lines = []
for line in file:
    lines.append(line)
    # lines.append(line.strip('\n'))
print(lines)
file.close()
