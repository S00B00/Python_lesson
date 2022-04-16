my_rating = [8, 8, 7, 6, 6, 5, 5, 5, 4, 3, 3, 2, 1]
new_number = int(input('Введите место в рейтинге: '))
i = 0
for n in my_rating:
    if new_number <= n:
        i += 1
my_rating.insert(i, new_number)
print(my_rating)