import requests
import random


class BasicWord():
    def __init__(self, word, subwords):
        self.word = word
        self.subwords = subwords

    def checking_entered_words(self, user_word):
        return user_word in self.subwords  # проверка введенного слова в списке допустимых подслов (вернет bool)

    def word_count(self):
        return len(self.subwords)  # подсчет количества подслов

    def __repr__(self):
        return f'{self.word} {self.subwords}'


class Player():
    def __init__(self, user_name):
        self.user_name = user_name
        self.user_subwords_used = []

    def sum_subwords_used(self):
        return len(self.user_subwords_used)  # получение количества использованных слов (int)

    def add_used_subwords(self, user_word):
        self.user_subwords_used.append(user_word)  # добавление слова в использованные слова

    def if_the_word_was_used(self, word):
        return word in self.user_subwords_used  # проверка использования данного слова до этого (возвращает bool)

    def __repr__(self):
        return f'{self.user_name}, {self.user_subwords_used}'


# ________________________________________________________________________________________________________________
'''utils'''


def load_random_word():
    response = requests.get('https://www.jsonkeeper.com/b/KAVA').json()  # что бы можно было прочитать
    data = random.choice(response)
    word = data['word'].upper()
    subwords = data['subwords']
    return BasicWord(word, subwords)


# _________________________________________________________________________________________________________________
w = load_random_word()


def main():
    p = Player(input('Ввведите имя игрока\n'))
    print(f'Привет, {p.user_name}!')
    print(f'Составьте {w.word_count()} слов из слова {w.word}\n'
          f'Слова должны быть не короче 3 букв\n'
          f'Чтобы закончить игру, угадайте все слова или напишите "stop"\n'
          f'Поехали, ваше первое слово?')

    while p.sum_subwords_used() != w.word_count():
        user_input = input()
        if user_input == 'stop' or user_input == 'стоп':
            break

        if p.if_the_word_was_used(user_input):
            print('уже использовано')
            continue

        if w.checking_entered_words(user_input):
            print('верно')
            p.add_used_subwords(user_input)
        elif len(user_input) < 3:
            print('слишком короткое слово')
        else:
            print('неверно')

    print(f'Игра завершена, вы угадали {p.sum_subwords_used()} слов!')


main()
