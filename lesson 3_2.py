def print_data(name, surname, birthday, city, email, phone):
    return f'Имя = {name}, Фамилия = {surname}, Дата рождения = {birthday}, Город = {city}, эл.почта = {email}, телефон = {phone}'


print(print_data(name=input('Ваше имя: '), surname=input('Ваша фамилия: '), birthday=input('дата рождения: '),
                 city=input('ваш город: '), email=input('адрес эл.почты: '), phone=input('телефон: ')))