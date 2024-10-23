from utils import get_words, random_words


def main():
    user_name = input("Hi! Whats your name?")
    words = get_words("words.txt")
    print(f"Ok{user_name}, let's play,")
    points = 0
    for word in words:
        random_word = random_words(word)
        print(f"ges the word: {random_word}")
        answer = input("Your answer: ")
        if answer == word:
            print("you're right and get 10 points")
            points += 10
        else:
            print(f"You're not right, right answer {word}")
    print(f"Game over, gamer {user_name} gets {points} points")


if __name__ == "__main__":
    main()
