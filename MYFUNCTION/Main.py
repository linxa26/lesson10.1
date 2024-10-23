from Function import get_word, sample_word, random_word


def main():
    user_name = input("Привет, как тебя зовут? ")
    print(f"Привет, {user_name}, начинаем тренировку!")
    words = get_word("test.txt")
    points = 0
    random_choice_word = random_word(words)
    print(random_choice_word)
    for word in words:
        sampled_word = sample_word(word)
        print(f'Угадайте слово: {sampled_word}')
        user_input = input()
        if user_input == word:
            points += 10
            print(f"Верно, вы получаете 10 баллов")

        else:
            print(f"Неверно, правильный ответ {word}!")


if __name__ == "__main__":
    main()
