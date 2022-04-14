

# задание 4
my_str = input('Введите целое число: ')
max_number = int(my_str[0])
i = 1
while(i < len(my_str)):
    if(max_number < int(my_str[i])):
        max_number = int(my_str[i])
    i += 1
print(f'Наибольшая цифра в {my_str} равна {max_number}')

