class Matrix:
    def __init__(self, lists):
        self.lists = lists

    def __str__(self):
        return '\n'.join(map(str, self.lists))

    def __add__(self, other):
        c = []
        for i in range(len(self.lists)):
            c.append([])
            for j in range(len(self.lists[0])):
                c[i].append(self.lists[i][j] + other.lists[i][j])
        return Matrix(c)


my_matrix_1 = Matrix([[5, 2, 1, 6], [4, 4, 4, 5], [9, 0, 5, 0]])
my_matrix_2 = Matrix([[1, 7, 1, 2], [3, 2, 1, 2], [3, 4, 3, 1]])
print(my_matrix_1)
print(my_matrix_2)
s = my_matrix_1 + my_matrix_2
print(s)
