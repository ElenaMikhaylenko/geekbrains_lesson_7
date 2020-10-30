from copy import deepcopy


class Matrix:

    def __init__(self, matrix):
        self.matrix = deepcopy(matrix)

    def __str__(self):
        return '\n'.join('\t'.join(map(str, row))
                         for row in self.matrix)

    def __add__(self, other):
        result = deepcopy(self.matrix)
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                result[i][j] += other.matrix[i][j]
        return Matrix(result)


matrix_1 = Matrix([[31, 22], [37, 43], [51, 86]])
matrix_2 = Matrix([[3, 5], [2, 4], [-1, 64]])

print(matrix_1 + matrix_2)








