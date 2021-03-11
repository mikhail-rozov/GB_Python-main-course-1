# Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.

def err_msg():
    return 'Нужно было ввести одно слово из маленьких латинских букв!'


def is_valid(my_list):
    for i in range(0, len(my_list)):
        if 97 <= ord(my_list[i]) <= 122:  # Проверка на маленькие латинские буквы и отсутствие пробела
            continue
        else:
            return False
    return True


def int_func(my_str):
    my_str = list(my_str)
    if is_valid(my_str):
        my_str[0] = chr(ord(my_str[0]) - 32)       # Переводим маленький символ в большой
        my_str = ''.join(my_str)                   # Собираем строку из списка
        return my_str
    else:
        return err_msg()


word = input('Введите слово из маленьких латинских букв: ')
word = int_func(word)
print(word)
