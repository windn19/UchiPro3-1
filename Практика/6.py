import sys

files = {}

for line in sys.stdin:
    file = line.strip('\n')
    _, ext = file.split('.')
    if ext not in files:
        files[ext] = [file]
    else:
        files[ext].append(file)

for ext in sorted(files):
    for file in sorted(files[ext]):
        print(file)
    print(f'Количество файлов {ext}: {len(files[ext])}')
    print()
