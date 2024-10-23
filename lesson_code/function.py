import random


def get_words(filename: str):
    with open(filename, 'r') as file:
        return file.read().splitlines()


def shuffle_word(word: str):
    word_list = list(word)
    random.shuffle(word_list)
    return "".join(word_list)


def safe_score(filename: str, user_name: str, points: int):
    with open(filename, 'a') as file:
        file.write(f'{user_name} {points}\n')


def get_top_results(filename: str):
    with open(filename, 'r') as file:
        results = file.read().splitlines()
    games_count = 0
    top_points = 0
    for result in results:
        user_name, points = result.split()
        int_points = int(points)
        if top_points < int_points:
            top_points = int_points
    games_count += 1
    return {'games_count': games_count, 'top_points': top_points}