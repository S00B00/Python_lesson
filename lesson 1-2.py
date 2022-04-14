# задание 2
seconds = int(input('Введите кол-во секунд: '))
hours = seconds // 3600
minutes = seconds % 3600 // 60
seconds = seconds % 3600 % 60
print("это соответствует (чч:мм:сс):", '{}:{}:{}'.format(hours, minutes, seconds))
