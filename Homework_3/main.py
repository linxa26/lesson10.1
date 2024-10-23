from function import get_words


def main():
    user_name = input("Привет, введите номер студента")
    words = get_words('text.txt')
    points = 0

    for word in words:
        shuffled_word = shuffle_word(word)
        print(f'Угадайте слово: {shuffled_word}')
        user_input = input()
        if word == user_input:
            points += 10
            print(f"Верно, вы получаете 10 баллов")
        else:
            print(f"Неверно, правильный ответ {word}!")

    safe_score(filename='progress.txt', user_name=user_name, points=points)
    games_result = get_top_results('progress.txt')
    print(f'Всего игр сыграно: {games_result["games_count"]}')
    print(f'Максимальный рекорд: {games_result["top_points"]}')


if __name__ == "__main__":
    main()
