import random


def get_word(filename):
    with open(filename, "r") as file:
        return file.read().splitlines()


def random_word(words):
    return random.choice(words)


def sample_word(word):
    i = len(word)
    word_1 = random.sample(word, i)
    return ''.join(word_1)

