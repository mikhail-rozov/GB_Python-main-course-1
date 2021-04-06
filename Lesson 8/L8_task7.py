# Реализовать проект «Операции с комплексными числами». Создайте класс
# «Комплексное число», реализуйте перегрузку методов сложения и умножения
# комплексных чисел. Проверьте работу проекта, создав экземпляры класса
# (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.

class ComplexNumber:
    def __init__(self, real, imaginary=0):
        self.real = real
        self.imaginary = imaginary

    def __str__(self):
        if self.real == 0 and self.imaginary == 0:
            return '0'
        if self.real == 0:
            return f'{self.imaginary}j'
        if self.imaginary > 0:
            return f'{self.real}+{self.imaginary}j'
        elif self.imaginary < 0:
            return f'{self.real}{self.imaginary}j'
        else:
            return str(self.real)

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)

    def __mul__(self, other):
        return ComplexNumber(self.real * other.real - self.imaginary * other.imaginary,
                             self.real * other.imaginary + self.imaginary * other.real)


number_1 = ComplexNumber(6, -8)
number_2 = ComplexNumber(-4, 5)

print(f'{number_1 + number_2} - sum')
print(f'{number_1 * number_2} - product')
