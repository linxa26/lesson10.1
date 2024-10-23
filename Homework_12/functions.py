import json


def load_questions(file_name):
    with open(file_name, "r") as file:
        file_dict = json.load(file)
    return file_dict


