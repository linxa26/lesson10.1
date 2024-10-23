from my_function import get_sum

def main():
    user_name = input("Привет, как тебя зовут?")
    print(f"ок, {user_name}, давай начинать!")
    sum = get_sum('my_list.txt')

    print(f'сумма трат: {sum}')

if __name__ == "__main__":
    main()