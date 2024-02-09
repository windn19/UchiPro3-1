with open('text.txt', encoding='utf-8') as file:
    lines = file.readlines()

total = 0
for line in lines:
    line = line.strip('\n')
    if line.isdigit():
        total += int(line)

print('>>> ', total)
