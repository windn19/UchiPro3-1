from sys import stdin

total = 0
for line in stdin:
    line = line.strip('\n')
    if line.isdigit():
        total += int(line)

print('>>', total)
