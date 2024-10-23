import json
file_name = [
    {
        "pk": 1,
        "full_name": "Jane Snake",
        "skills": ["Python", "Go", "Linux"]
    },
    {
        "pk": 2,
        "full_name": "Sheri Torres",
        "skills": ["Java", "Swify", "Fortran", "Basic"]
    },
    {
        "pk": 3,
        "full_name": "Burt Stein",
        "skills": ["Planning", "Negotiation", "Management", "Sales"]
    },
    {
        "pk": 4,
        "full_name": "Bauer Adkins",
        "skills": ["HTML", "CSS", "JavaScript", "React", "Node.js"]
    }
]

proffession_list = [
    {
        "pk": 1,
        "title": "Backend",
        "skills": ["Python", "Linux", "Docker", "SQL", "Flask"]
    },
    {
        "pk": 2,
        "title": "Frontend",
        "skills": ["HTML", "CSS", "React", "JavaScript"]
    },
    {
        "pk": 3,
        "title": "Testing",
        "skills": ["Windows", "MacOS", "SQL", "Jira"]
    }
]


def my():
    filename = "professions.json"
    with open(filename, 'r') as file:
        data = json.load(file)
        questions = {}
    for item in data:
        text = item['pk']
        difficulty = item['title']
        wright_answer = item['skills']
        question = {text: {difficulty: wright_answer}}
        questions = question
    return questions[3]





print(my())
