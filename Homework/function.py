import random


def get_words(file):
    with open(file, "r") as file:
        return file.read().splitlines()


def sample_word(word):
    i = len(word)
    word = random.sample(word, i)
    return ''.join(word)


def safe_score(file_name, user_name, points):
    with open(file_name, "a") as file:
        file.write(f"{user_name} {points}\n")


def top_result(file_name):
    with open(file_name, "r") as file:
        results = file.read().splitlines()
    game_point = 0
    top_point = 0
    for result in results:
        user_name, points = result.split()
        int_points = int(points)

        if top_point < int_points:
            top_point = int_points
        game_point += 1

    return (f'Всего игр сыграно: {game_point}, лучший результат:{user_name}:{top_point}')
