# Создать текстовый файл (не программно), сохранить в нём несколько строк,
# выполнить подсчёт строк и слов в каждой строке.

with open('text_1.txt', 'r', encoding='utf-8') as f:
    text = f.readlines()

print(f'Число строк в текстовом файле: {len(text)}')

for i, el in enumerate(text):
    el = el.replace('\n', '')
    el = el.split()
    word_number = 0
    for word in el:
        if word.isalpha():
            word_number += 1
    print(f'В строке {i + 1} находится {word_number} слов.')
