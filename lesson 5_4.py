my_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
with open('5_4.txt', 'r', encoding='utf-8') as f:
    with open('5_4_1.txt', 'w', encoding='utf-8') as f2:
        f2.writelines([line.replace(line.split()[0], my_dict.get(line.split()[0])) for line in f])
