# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

import random


with open('text_5.txt', 'w+', encoding='utf-8') as f:
    for i in range(10):
        f.write(str(random.randint(-100, 100)) + ' ')
    f.seek(0)
    numbers = f.readline()

numbers = numbers.split()
numbers = [int(number) for number in numbers]

print(sum(numbers))
