import random

from data import questions_data


class Question():
    def __init__(self, question_text, question_diff, question_answer):
        self.question_text = question_text  # текст вопроса
        self.question_diff = question_diff  # сложность вопроса int
        self.question_answer = question_answer  # верный вариант ответа

        self.is_asked = False  # задан ли вопрос
        self.user_answer = None  # ответ пользователя
        self.point = self.question_diff * 10  # баллы за вопроc

    def get_points(self):
        return self.point

    def is_correct(self):
        return self.user_answer == self.question_answer

    def build_question(self):
        return f'\nВопрос:{self.question_text}\nСложность {self.question_diff}/5'

    def build_positive_feedback(self):
        return f'Ответ верный, получено {self.point} баллов'

    def build_negative_feedback(self):
        return f'Ответ неверный, верный ответ {self.question_answer}'

    def __repr__(self):
        return f'{self.question_text} - {self.question_answer} {self.question_diff}/5'


# ____________________________________________________________________________________________________

def main():
    questions = [Question(question['q'], question['d'], question['a']) for question in questions_data]

    print('Игра начинается!')
    random.shuffle(questions)

    correct_counter = 0
    points = 0

    for q in questions:
        print(q.build_question())
        q.user_answer = input()

        if q.is_correct():
            print(q.build_positive_feedback())
            correct_counter += 1
            points += q.get_points()
        else:
            print(q.build_negative_feedback())

    print(f'\nВот и всё!\nОтвечено {correct_counter} вопроса из {len(questions)}\nНабрано баллов: {points}')


main()
