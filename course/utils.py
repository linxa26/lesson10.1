# Функция загрузки набора слов и выбора случайного
def load_random_word(path: str):
    import requests
    """
    Функция:
    — получает список слов с внешнего ресурса,
    — выбирает случайное слово,
    — создаёт экземпляр класса `BasicWord`.
    :param path: str
        ссылка на источник.
    :return: BasicWord
    """
    from random import choice
    from requests import get
    from basic_word import BasicWord

    random_word_dict = choice(get(path).json())

    # return BasicWord(random_word_dict['word'], list(set(random_word_dict['subwords']))) # С избавлением от дублей
    return BasicWord(random_word_dict['word'], random_word_dict['subwords'])


# Функция печати статистики игры
def print_results(used_words_number: int, valid_words_number: int):
    """
    Функция печатает статистику игры
    :param number: int
        кол-во верно угаданных слов
    :return: None
    """
    if used_words_number == valid_words_number:
        print(f"\nСлова закончились, игра завершена!")
    else:
        print(f"\nИгра завершена!")
    if used_words_number % 100 in [11, 12, 13, 14]:
        print(f"Вы угадали {used_words_number} слов!")
    elif used_words_number % 10 in [2, 3, 4]:
        print(f"Вы угадали {used_words_number} слова!")
    elif used_words_number % 10 == 1:
        print(f"Вы угадали {used_words_number} слово!")
    else:
        print(f"Вы угадали {used_words_number} слов!")


# Функция для тестирования функций и классов на работоспособность
def test_classes():
    """
    Функция для тестирования функций и классов на работоспособность
    """
    from players import Player
    from basic_word import BasicWord

    # Тесты
    # Создаем экземпляр класса с именем Татошка
    player = Player("Татошка")

    # Проверяем док-стринги
    print(f"{player.__doc__}\n")

    # Проверяем __repr__
    print(f"{player}\n")

    # Проверяем добавление слова, и получение количества слов
    player.add_used_word("Полянка")
    print(f"Использовано слов: {str(player.used_words_count())} :: {player}")
    player.add_used_word("Дудочка")
    print(f"Использовано слов: {str(player.used_words_count())} :: {player}\n")

    # Проверяем проверку слов на использованность
    print(f"Проверка слова Дудочка: {str(player.is_used_word('Дудочка'))}")
    print(f"Проверка слова Кувшинчик: {str(player.is_used_word('Кувшинчик'))}")

    basic_word = BasicWord("автомобиль",
                           ['молитва', 'альбом', 'вомбат', 'ломота', 'ломоть', 'мольба', 'битва', 'ботва', 'вобла'])

    # Проверяем док-стринги
    print(f"{basic_word.__doc__}\n")

    # Проверяем __repr__
    print(f"{basic_word}\n")

    # Проверяем находится ли введенное слово в списке допустимых подслов (вернет bool)
    assert basic_word.check("ломота") is True, "Метод check работает некорректно"
    assert basic_word.check("локомотив") is False, "Метод check работает некорректно"

    # Проверяем подсчет кол-ва слов
    assert basic_word.len_valid() == len(basic_word.valid_words), "Метод len_valid работает некорректно"

    # Проверка работы функции
    path = "https://jsonkeeper.com/b/ZFRD"
    word = load_random_word(path)
    print(f"Слово: {word.original_word}")
    print(f"Список валидных слов: {word.valid_words}")