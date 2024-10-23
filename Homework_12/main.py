from functions import load_questions




class Question():


    def get_points(self):

        print("Привет, игра начинается, вот тебе первый вопрос: ")
        questions = load_questions('question.json')
        print(questions)


