import random


def lol(file_name):
    with open(file_name, "r") as file:
        words = file.read().splitlines()
        return words


def sample_word(ramdom_words):
    i = len(ramdom_words)
    sample_words = random.sample(ramdom_words, i)
    return ''.join(sample_words)


def statistic(user_name, point):
    with open("statistic.txt", "a") as file:
        file.write(f'{user_name} {point} \n')


def top_result(file_name):
    top_score = 0
    with open(file_name, "r") as file:
        results = file.read().splitlines()
    for result in results:
        user_name, point = result.split()
        int_point = int(point)
        if top_score < int_point:
            top_score = int_point

    return f'лучший результат:{top_score}'
