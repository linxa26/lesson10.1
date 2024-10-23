class BasicWord:
    """
    Класс BasicWord содержит:
    - исходное слово,
    - список допустимых подслов,
    Методы:
    - проверка введенного слова в списке допустимых подслов (вернет bool),
    - подсчет количества подслов (вернет int)
    """

    # Инициализируем поля: исходное слово, список допустимых подслов
    def __init__(self, original_word, valid_words):
        self.original_word = original_word
        self.valid_words = valid_words

    # Печатаем информацию об экземпляре класса
    def __repr__(self):
        return f"Слово: {self.original_word}\nСписок подслов: {self.valid_words}"

    # Проверяем использование исходного слова в списке допустимых подслов (возвращает bool)
    def check(self, word):
        return word in self.valid_words

    # Выполняем подсчет количества подслов (вернет int)
    def len_valid(self):
        return len(self.valid_words)