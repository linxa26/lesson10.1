"""
Курсовая работа
"""
import random

# Шаг 0 составил список английских слов

words = ["one", "two", "three", "four", "five"]

answers = []

morse_dict = {
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    "!": "-.-.--",
    "-": "-....-",
    "/": "-..-.",
    "@": ".--.-.",
    "(": "-.--.",
    ")": "-.--.-"
}


# шаг 1 переводим слова в азбуку морзе
def morse_encode(enter_words):
    encoded_words = []
    for x in enter_words:
        encoded_words.append(morse_dict[x])
    return "".join(encoded_words)


# шаг 2 C помощью функции get_word получаем случайное число
def get_word(words):
    random_word = random.choice(words)
    return random_word


# Шаг 3 считаем статистику
def statistic_game(answers):
    score_true = 0
    score_false = 0

    for x in answers:
        if x == True:
            score_true += 1
        else:
            score_false += 1
    print(f'всего слов {len(answers)}')
    print(f'правильных ответов: {score_true}')
    print(f'неправильных ответов: {score_false}')


# Шаг 4 Программа входит в контакт с пользователем
print("Сегодня мы потренируемся расшифровывать морзянку")
print(input("Введите Enter и мы начнем!"))

# Шаг 5. Запускаем цикл задавания вопросов
for x in range(1, 6):
    enter_words = get_word(words)
    morse = morse_encode(enter_words)
    print(morse)

    user = input()

    if user == enter_words:
        answers.append(True)
        print(f"Верно,{user}!")

    else:

        answers.append(False)
        print(f"Неверно, {enter_words}!")

statistic_game(answers)