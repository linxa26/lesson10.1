from Functions import load_professions, load_students, et_student_by_pk, et_profession_by_pk


def main() -> object:
    """

    :rtype: object
    """
    user_type = int(input("Привет, введите номер студента "))
    if user_type == 1 and 2 and 3 and 4:
        student_list = load_students("students.json")
        y = int(user_type - 1)
        student_info = et_student_by_pk(student_list, y)
        print(student_info)
        student_profession = load_professions("professions.json")
        user_type_1 = input(f"Выбирете специальность для оценки студента {student_info[7:20]} \n")
        if user_type_1 == "Backend":
            profession_info = et_profession_by_pk(student_list, student_profession, y, 0)
            print(profession_info)
        elif user_type_1 == "Frontend":
            profession_info = et_profession_by_pk(student_list, student_profession, y, 1)
            print(profession_info)
        elif user_type_1 == "Testing":
            profession_info = et_profession_by_pk(student_list, student_profession, y, 2)
            print(profession_info)
    else:
        print("Нет такого студента")


if __name__ == "__main__":
    main()
