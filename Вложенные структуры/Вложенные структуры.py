import json


def load_students():
    with open('students.json', 'r', encoding='utf-8') as file:
        return json.load(file)


def load_professions():
    with open('professions.json', 'r', encoding='utf-8') as file:
        return json.load(file)


def get_student_by_pk(pk):
    user_data = int(input('Введите номер студента\n'))
    for n in pk:
        if user_data == n["pk"]:
            return n
    print('У нас нет такого студента')
    return


def get_profession_by_title(title):
    user_data = input().title()
    for t in title:
        if user_data == t["title"]:
            return t
    return None


def check_fitness(student, profession):
    student_skills = set(student["skills"])
    profession_skills = set(profession["skills"])
    lacks_skills = profession_skills - student_skills  # не хватает скиллов
    has_skills = student_skills.intersection(profession_skills)  # имеет скиллы
    fit_percent = int((len(has_skills) / len(profession_skills)) * 100)  # разница по скиллам в %
    return {"has": list(has_skills), "lacks": list(lacks_skills), "fit_percent": fit_percent}


# =========================================================================================================

def main():
    students = get_student_by_pk(load_students())
    if students is None:
        return
    print(f'Студент {students["full_name"]}\nЗнает {", ".join(students["skills"])}')

    print(f'Выберите специальность для оценки студента {students["full_name"]}')
    title = get_profession_by_title(load_professions())
    if title is None:
        print('У нас нет такой специальности')
        return

    fit_info = check_fitness(students, title)
    print(f'Пригодность {fit_info["fit_percent"]}%')
    print(f'{students["full_name"]} знает {", ".join(fit_info["has"])}')
    print(f'{students["full_name"]} не знает {", ".join(fit_info["lacks"])}')


main()
