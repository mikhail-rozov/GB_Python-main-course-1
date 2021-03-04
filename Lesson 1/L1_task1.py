# Поработайте с переменными, создайте несколько,
# выведите на экран, запросите у пользователя несколько
# чисел и строк и сохраните в переменные, выведите на экран.

pi = 3.14
color = 'black'
age = 44

print(pi)
print(type(pi))
print(color)
print(type(color))
print(age)
print(type(age))

name = input('What is your name? ')
age = int(input('How old are you? '))

print(f'Hi, {name}! In five years you will be {age + 5} years old!')
