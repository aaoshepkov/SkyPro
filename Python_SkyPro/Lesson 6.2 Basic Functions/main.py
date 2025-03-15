'''
создаем нужные для игры словари, созданные по 3-м логическим типам -
легкие слова, средние слова, сложные слова.
Также создаем словарь levels, который хранит оценки за ответы
'''
words_easy = {
    "family":"семья",
    "hand": "рука",
    "people":"люди",
    "evening": "вечер",
    "minute":"минута",
}

words_medium = {
    "believe":"верить",
    "feel": "чувствовать",
    "make":"делать",
    "open": "открывать",
    "think":"думать",
}

words_hard   = {
    "rural":"деревенский",
    "fortune": "удача",
    "exercise":"упражнение",
    "suggest": "предлагать",

    "except":"кроме",
}

levels = {
   0: "Нулевой",
   1: "Так себе",
   2: "Можно лучше",
   3: "Норм",
   4: "Хорошо",
   5: "Отлично",
}


'''
объявляем функцию для ввода пользователем уровня сложности, на котором он хотел бы поиграть. 
Функция возвращает словарь согласно выбранному уровню.
'''
def choose_difficulty():
    level = input('Выберите уровень сложности (легкий, средний, сложный): ')
    level = level.lower()
    if level == 'легкий':
        words = words_easy
    elif level == 'средний':
        words = words_medium
    elif level == 'сложный':
        words = words_hard
    else:
        words = words_medium
    return words

words_to_play = choose_difficulty()


'''
объявляем функцию, которая перебирает словарь, соответствующий выбранному пользователем 
уровню сложности, и предлагает ввести перевод слова(ключа).
Все верные ответы, записываем в созданный словарь answers со значение True, неверные с False
'''
answers = {}
def play_game(text):
    for word, value in text.items():
        print(f'{word}, {len(value)} букв, начинается на {value[0]}...')
        answer = input(f'Введите ваш ответ: ')
        if answer.lower() == value.lower():
            print(f'Верно. {word.capitalize()} - это {value.lower()}')
            answers[word] = True
        else:
            print(f'Неверно. {word.capitalize()} - это {value.lower()}')
            answers[word] = False
    return answers

results = play_game(words_to_play)


'''
объявляем функцию для вывода верных и неверных ответов.
'''
def display_results(res):
    right_answers = {}
    wrong_answers = {}
    for word, answer in res.items():
        if answer is True:
            right_answers[word] = answer
        if answer is False:
            wrong_answers[word] = answer

    right_answers = list(right_answers.keys())
    wrong_answers = list(wrong_answers.keys())
    print(f'Правильно отвечены слова:\n{'\n'.join(right_answers)}')
    print(f'Неправильно отвечены слова:\n{'\n'.join(wrong_answers)}')

display_results(results)


'''
в этой функции считаем уровень по количеству верных ответов.
'''
def calculate_rank(text):
    result = 0
    for value in text.values():
        if value is True:
            result += 1
        else:
            continue
    return levels[result]
users_result = calculate_rank(results)

print(f'Ваш ранг:\n{users_result}')