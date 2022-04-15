def my_share(a, b):
    try:
        return float(a) / float(b)
    except ZeroDivisionError:
        print('Второе число не может быть = 0')
    except ValueError:
        print('Нужно вводить числа, дробную часть отделять "."')


print(my_share(input('Введите первое число: '), input('Введите второе число: ')))
