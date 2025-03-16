# #гетерогенный список - содержит разные типы данных
# # list1 = [1, 250, 'первый', 'second', True, False]
#
# # for i in range(len(list1)):
# #     print(i)
# #print(len(list1))
#
# # for i in len(list1):
# #     print(i)
# #
# # for i, y in enumerate(list1):
# #     print(i, y)
# # #
# # while True:
# #     if input('Please input: ') == '+':
# #         break
# #     print('-')
#
#
# # while 10 > value:
# #     value = 0
# #     value += 1
# #     print(value)
#
# # while True:
# #     for i in items:
# #         break
#
# text = input("Введите слово или фразу: ")
# vowels = "aeiou"
# vowel_indices = []
#
# vowels = list(vowels)
#
# for i, y in enumerate(text):
#     if y in vowels:
#         vowel_indices.append(i)
#
#
#
# # Не удаляйте и не изменяйте код ниже. Он нужен для проверки
# if vowel_indices:
#     print("Индексы гласных букв:", vowel_indices)
# else:
#     print("В тексте нет гласных букв.")

# from math import sqrt
# num = int(input())
#
# while True:
#     if num == 0:
#         print('NO')
#     elif num == 1:
#         print('YES')
#     elif round(sqrt(2)**2) % 10 == 0:
#         print('YES')
#     elif num == 0:
#         print('YES')
#
#
#     else:
#         print('NO')
#     break

# for i in range(10):
#     print(2**i)

# text = 'Сегодня 8 марта 2025 года. Дорогие дамы, С ПРАЗДНИКОМ ВАС!!!'
# vowels = 'аеёиоуыэюя'
#
# letters_count = 0
# digits_count = 0
# spaces_count = 0
# uppers_count = 0
# vowels_count = 0
#
# for char in text:
#     if char.isalpha():
#         letters_count += 1
#         if char.isupper():
#             uppers_count += 1
#         if char.lower() in vowels:
#             vowels_count += 1
#     elif char.isdigit():
#         digits_count += 1
#     elif char == ' ':
#         spaces_count += 1
#
#
# print(f'''Количество букв составляет: {letters_count}
# Количество цифр составляет на новой строке: {digits_count}
# Количество пробелов составляет: {spaces_count}
# Колчество букв в верхнем регистре: {uppers_count}
# Количество гласных букв: {vowels_count}''')



# text_to_count = "Статья рассказывает о последних научных статья об открытиях в области исследования космоса и опять статья. Интересно, что исследователи утверждают, что космическое время может быть относительным, а может быть статья."
# word_for_search = 'статья'
#
# word_count = text_to_count.lower().count(word_for_search)
#
# print(f'Слово {word_for_search} встречается {word_count} раз')


text_to_count = "Статья рассказывает о последних научных статья об открытиях в области исследования космоса и опять статья. Интересно, что исследователи утверждают, что космическое время может быть относительным, а может быть статья."
text_to_count = text_to_count.lower()
word_for_search = 'статья'
position= text_to_count.find(word_for_search)
position_count = 0
while position != -1:
    position_count += 1
    position= text_to_count.find(word_for_search, position + 1)


print(f'Слово {word_for_search} встречается {position_count} раз')