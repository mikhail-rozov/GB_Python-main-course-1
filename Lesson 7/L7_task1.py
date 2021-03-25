# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов
# класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой
# матрицы складываем с первым элементом первой строки второй матрицы и т.д.

class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        result = ''
        for el_list in self.matrix:
            for i, number in enumerate(el_list):
                result += str(number) + ' '
                if i == len(el_list) - 1:
                    result += '\n'
        return result

    def __add__(self, other):
        new_row_1 = [self.matrix[0][i] + other.matrix[0][i] for i in range(len(self.matrix[0]))]
        new_row_2 = [self.matrix[1][i] + other.matrix[1][i] for i in range(len(self.matrix[1]))]
        new_row_3 = [self.matrix[2][i] + other.matrix[2][i] for i in range(len(self.matrix[2]))]

        new_matrix = [new_row_1, new_row_2, new_row_3]
        return Matrix(new_matrix)


m_1 = Matrix([[1, 2], [3, 4], [5, 6]])
m_2 = Matrix([[5, 6], [3, 10], [3, 3]])
print(f'Матрица № 1:\n{m_1}')
print(f'Матрица № 2:\n{m_2}')
print(f'Сумма двух матриц равна:\n{m_1 + m_2}')
