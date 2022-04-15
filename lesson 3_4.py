def my_func(x, y):
    try:
        x = float(x)
        y = int(y)
    except ValueError:
        print('введите X - действительное число, Y - целое число')
        return
    if x <= 0 or y >= 0:
        print('X - положительное число, а Y - отрицательное число')
        return
    return x ** y


print(round(
    my_func(input('Введите действительное положительное число X: '), input('Введите целое отрицательное число Y: ')), 5))
