from function import get_words, sample_word, safe_score, top_result


def main():
    user_name = input("Привет, как тебя зовут?")
    print(f"Привет, {user_name}, начинаем тренировку!")
    words = get_words('words.txt')
    points = 0

    for word in words:
        sampled_word = sample_word(word)
        print(f'Угадайте слово: {sampled_word}')
        user_input = input()

        if user_input == word:
            points += 10
            print(f"Верно, вы получаете {points} баллов")

        else:
            print(f"Неверно, правильный ответ {word}!")

    safe_score(file_name='history.txt', user_name=user_name, points=points)
    game_result = top_result(file_name="history.txt")
    print(game_result)


if __name__ == "__main__":
    main()
