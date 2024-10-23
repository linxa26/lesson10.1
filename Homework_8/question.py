class Question:
    def __init__(self, text, difficulty, wright_answer):

        self.text = text
        self.difficulty = difficulty
        self.wright_answer = wright_answer
        self.is_asked = False
        self.user_answer = None
        self.score = self.difficulty * 10

    def get_points(self):
        return self.score

    def is_correct(self):
        return self.wright_answer == self.user_answer

    def build_question(self):
        return f'Вопрос: {self.text} \n' \
               f'Сложность: {self.difficulty} / 5'

    def build_feedback(self):
        if self.is_correct():
            return f'Ответ верный, получено {self.score} баллов'
        else:
            return f'Ответ неверный, верный ответ {self.wright_answer}'

