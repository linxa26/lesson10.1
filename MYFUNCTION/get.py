import random


def my(x):
    with open(x, "r") as file:
        y = file.read().splitlines()
        return random.choice(y)



