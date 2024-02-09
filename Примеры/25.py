with open('text.txt', encoding='utf-8') as file_input, open('output.txt', 'a', encoding='utf-8') as file_output:
        lines = file_input.readlines()
        for line in lines:
            if line.strip('\n').isdigit():
                file_output.write(line)
