from random import  randint

with open('5_5.txt', 'w', encoding='utf-8') as f:
    f.write(' '.join([str(randint(1, 100)) for _ in range(50)]))

with open('5_5.txt', 'r', encoding='utf-8') as f:
    numbers = [int(i) for i in f.read().split()]
    print(sum(numbers))