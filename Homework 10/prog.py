from function import lol, sample_word, statistic, top_result


def main():
    user_name = input('Привет! Как тебя зовут?')
    lol_1 = lol("words.txt")
    print(f"{user_name}, давай поиграем,")
    games = 0
    point = 0
    for word in lol_1:
        lol_2 = sample_word(word)
        print(f"угадай слово:{lol_2}")
        lol_3 = input("Ответ: ")

        if lol_3 == word:
            point += 10
            games += 1
            print("Верный ответ")
        else:
            games += 1
            print(f"Не верно, правильный ответ:{word}")

    statistic(user_name, point)
    top_statistic = top_result(file_name="statistic.txt")
    print(f"Вот и все, игра окончена! игрок: {user_name} набрал очков: {point}")
    print(top_statistic)


if __name__ == "__main__":
    main()
