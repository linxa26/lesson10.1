import json
from question import Question


def load_questions(filename):
    user_name = input("Привет, как тебя зовут?")
    print(f"ок, {user_name}, давай начинать!")
    with open(filename, 'r') as file:
        data = json.load(file)
    questions = []

    for item in data:
        text = item['q']
        difficulty = int(item['d'])
        wright_answer = item['a']
        question = Question(text, difficulty, wright_answer)
        questions.append(question)

    return questions


def build_statistic(questions):
    score = 0
    count = 0
    for question in questions:
        if question.is_correct():
            score = score + question.score
            count = count + 1
    return f'Вот и все! \n ' \
           f'Отвечено {count} вопроса из 5 \n' \
           f'Набрано баллов: {score}'


