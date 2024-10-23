from players import Player
from utils import load_random_word, print_results


def main():
    # Определяем настроечные переменные
    # path = "https://jsonkeeper.com/b/ZFRD" # Полный набор слов
    # path = "https://jsonkeeper.com/b/5OXK" # Набор слов из примера (с двойным скатом)
    path = "https://jsonkeeper.com/b/QJ5Q" # Укороченный список
    is_game_stopped = False

    # Спрашиваем имя пользователя и создаем объект игрока
    player = Player(input("Введите имя игрока: ").strip())
    # Получаем случайное слово для игры
    word = load_random_word(path)

    # Приветствуем игрока и начинаем игру
    print(f"\nПривет, {player.name}")
    print(f"Составьте {word.len_valid()} слов из слова \"{word.original_word}\"")
    print(f"Слова должны быть не короче 3 букв")
    print(f"Чтобы закончить игру, угадайте все слова или напишите \"stop\"")
    print(f"Поехали, ваше первое слово?")

    # Цикл, пока количество угаданных слов не сравняется с количеством слов, которые можно составить.
    # В каждой итерации получаем от пользователя слово, выполяем несколько проверок:
    # - Если слово короче 3 букв – это неудачное слово.
    # - Если слова нет в списке допустимых у BasicWord – это неудачное слово.
    # - Если слово уже было угадано пользователем (Player) – это неудачное слово.
    # - Если слово `stop` или `стоп`, то игра прекращается.
    while player.used_words_count() < word.len_valid() and not is_game_stopped:
        user_word = input("\nВведите слово: ").strip().lower()
        if len(user_word) < 3:
            print("Слишком короткое слово")
        elif user_word == "стоп" or user_word == "stop":
            is_game_stopped = True
        elif player.is_used_word(user_word):
            print("Уже использовано")
        elif not word.check(user_word):
            print("Неверно")
        else:
            print("Верно")
            player.add_used_word(user_word)

    # Выводим статистику игры
    print_results(player.used_words_count(), word.len_valid())


if __name__ == '__main__':
    main()