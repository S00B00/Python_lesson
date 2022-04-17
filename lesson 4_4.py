my_dict = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
d = {}
for i in my_dict:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
print([el for el in my_dict if d[el] == 1])

