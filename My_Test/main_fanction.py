from main_class import Main
import random


def test():
    lol = ["Вася", "Петя"]
    random.shuffle(lol)

    return lol


def test_1(lol):
    for i in lol:
        print(i)
