season_list = ['winter', 'winter', 'spring', 'spring', 'spring', 'summer', 'summer', 'summer', 'autumn', 'autumn', 'autumn', 'winter']
season_dict = {1 : 'winter', 2 : 'winter', 3 : 'spring', 4 : 'spring', 5 : 'spring', 6 : 'summer', 7 : 'summer', 8 : 'summer', 9 : 'autumn', 10 : 'autumn', 11 : 'autumn', 12 : 'winter'}
month = int(input('Введите номер месяца: '))
if month > 0 and month < 13:
    print(season_list[month - 1])
    print(season_dict.get(month))
else: print('В году 12 месяцев')