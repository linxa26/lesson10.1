import json


def load_students(file_name):
    with open(file_name, "r") as file:
        file_dict_1 = json.load(file)
    return file_dict_1


def load_professions(file_name):
    with open(file_name, "r") as file:
        file_dict_2 = json.load(file)
    return file_dict_2


def et_student_by_pk(file_name, y):
    return (f"Студент: {file_name[y]['full_name']}\nЗнает: {', '.join(file_name[y]['skills'])}")


def et_profession_by_pk(student_list, student_profession,y,x):

    file_dict_1 = {""}
    file_dict_3 = {""}
    file_dict = student_list[y]["skills"]
    for i in file_dict:
        file_dict_1.add(i)
        file_dict_2 = student_profession[x]["skills"]
    for i in file_dict_2:
        file_dict_3.add(i)
    return (f"Пригодность: {100 - (len((file_dict_3.difference(file_dict_1)))*(round(100/len(file_dict_2))))}%"
            f"\nСтудент знает: {' '.join(file_dict_3.intersection(file_dict_1))}"
            f"\nСтудент не знает: {' '.join(file_dict_3.difference(file_dict_1))}")

