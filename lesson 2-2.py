my_list = input('Введите значения через пробел: ').split()
for i in range(1, len(my_list), 2): #выбираем значения с нечетными индексами
    my_list[i - 1], my_list[i]  = my_list[i], my_list[i - 1] #меняем значения местами
print(my_list)
