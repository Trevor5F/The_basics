import random


def words():
    with open('words.txt', encoding='utf-8') as file:
        return file.read().splitlines()


# def shuffle_word():
#     for word in words():
#         word_list = list(word)
#         random.shuffle(word_list)
#         print(''.join(word_list))

shuffled_words = lambda word: ''.join(random.sample(word, len(word)))


def history_write(name, integ):
    with open('history.txt', 'a', encoding='utf-8') as file:
        file.write(f'{name} {integ}\n')


def history():
    with open('history.txt', encoding='utf-8') as file:
        x = [i.strip().split(' ')[-1] for i in file]

        max_score = max(x)
        len_score = len(x)

        return {'max': max_score, 'len': len_score}


def main():
    user_score = 0

    user_name = input('Введите ваше имя\n')

    for word in words():
        print('Угадайте слово:', shuffled_words(word))
        user_input = input()
        if user_input == word:
            print('Верно! Вы получаете 10 очков.\n')
            user_score += 10
        else:
            print(f'Неверно! Верный ответ – {word}.\n')

    history_write(user_name, user_score)

    print(f'\nВсего игр сыграно: {history().get("len")}')
    print(f'Максимальный рекорд: {history().get("max")}')


main()
