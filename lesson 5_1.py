out_f = open("out_file.txt", "w", encoding="utf-8")
while (line := input('Введите строку данных, по окончании введите "Enter": ')) !='':
    out_f.write(f'{line}\n')
out_f.close()

