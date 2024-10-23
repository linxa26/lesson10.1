import random


def get_words(file_name):
    with open(file_name, "r") as file:
        words = file.read().splitlines()
        return words


def random_words(file):
    i = len(file)
    random_word = random.sample(file, i)
    return ''.join(random_word)









