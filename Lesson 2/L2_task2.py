# Для списка реализовать обмен значений соседних элементов, т.е. Значениями
# обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве
# элементов последний сохранить на своем месте. Для заполнения списка элементов
# необходимо использовать функцию input().

elements_quantity = int(input('Enter the number of elements in the list: '))
the_list = []

for i in range(0, elements_quantity):
    the_list.append(input(f'Enter element # {i}: '))

print(f'The list is:\n{the_list}\n')

for i in range(1, len(the_list), 2):
    the_list[i], the_list[i-1] = the_list[i-1], the_list[i]

print(f'The list with switched elements is:\n{the_list}')
