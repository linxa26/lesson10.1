import random
from function import load_questions, build_statistic

if __name__ == "__main__":
    filename = 'questions.json'
    questions = load_questions('questions.json')

    random.shuffle(questions)

    for question in questions:
        print(question.build_question())
        user_answer = input('Ответ:')
        question.user_answer = user_answer
        print(question.build_feedback())

    print('')
    print(build_statistic(questions))
