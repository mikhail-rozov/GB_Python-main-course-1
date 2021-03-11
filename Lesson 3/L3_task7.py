# Продолжить работу над заданием. В программу должна попадать строка из слов, разделённых пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре. Нужно сделать вывод исходной строки,
# но каждое слово должно начинаться с заглавной буквы. Используйте написанную ранее функцию int_func().

def err_msg():
    return 'Нужно было ввести слова из маленьких латинских букв!'


def is_valid(my_list):
    for i in range(0, len(my_list)):
        if 97 <= ord(my_list[i]) <= 122:
            continue
        else:
            return False
    return True


def int_func(my_str):
    my_str = list(my_str)
    if is_valid(my_str):
        my_str[0] = chr(ord(my_str[0]) - 32)
        my_str = ''.join(my_str)
        return my_str
    else:
        return err_msg()


sentence = input('Введите строку из слов в нижнем регистре из латинских букв: ')
sentence = sentence.split()
for index, value in enumerate(sentence):
    if int_func(value) == err_msg():
        sentence = err_msg()
        break
    else:
        sentence[index] = int_func(value)
if sentence != err_msg():
    sentence = ' '.join(sentence)
print(sentence)
