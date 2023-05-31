import requests
import json
import csv

#Функ-я логіну користувача
def authentication(login: str, password: str):
    response = requests.post("https://ksu24.kspu.edu/api/v2/login/",
                             data={"username": login, "password": password})
    if response.ok:
        print("Вхід виконано!")
    else:
        print(f"Вхід не виконаний! Перевірте правильність Логіну та Пароля! \nКод Помилки: {response.status_code} \nТекст Помилки:{response.text}")

    try:
        cookie = response.cookies.get_dict()["JWT"]
        return cookie
    except KeyError:
        print("Не вдалося отримати доступ до кукі")
        return None

#Функ-я отримання значень результату запиту через API
def get_value(url: str, cookie: str, key: str, filter_by: dict = None):
    response = requests.get(url=url, cookies={"JWT": cookie})
    response.raise_for_status()

    data = response.json()
    for item in data.get("results", [data]):
        if filter_by and item.get(list(filter_by.keys())[0]) != filter_by.get(list(filter_by.keys())[0]):
            continue
        if key in item:
            return item[key]
    if filter_by is None:
        print("This key doesn't exist...")
    else:
        print("No information found for the specified filter...")
    return None

#Функ-я отримання інформації з API з фільтрацією
def get_info(url: str, cookie: str, filter_by: dict = None):
    response = requests.get(url=url, cookies={"JWT": cookie})
    response.raise_for_status()

    data = response.json()
    results_list = data.get("results", [data])
    for dictionary in results_list:
        if filter_by is not None:
            filtered_dict = {key: value for key, value in dictionary.items() if key in filter_by}
        else:
            filtered_dict = dictionary
        for key, value in filtered_dict.items():
            print(f"{key}: {value}")
        print("-" * 30)

        #Збереження даних у форматі JSON
        with open('data.json', 'a') as json_file:
            json.dump(filtered_dict, json_file)
            json_file.write('\n')

        #Збереження даних у форматі CSV
        with open('data.csv', 'a', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(filtered_dict.values())

#Функ-я розрахунку балу
def calculate_average(data_list, key):
    total = 0
    count = 0
    for data in data_list:
        if key in data:
            total += data[key]
            count += 1
    if count > 0:
        return total / count
    else:
        return None

def main():
    ksu_24_student = "https://ksu24.kspu.edu/api/v2/my/students/"
    ksu_24_profile = "https://ksu24.kspu.edu/api/v2/my/profile/"
    login = input("Введіть ваш логін: ")
    password = input("Введіть ваш пароль: ")
    # Запит на логін\пароль
    cookie = authentication(login=login, password=password)
    if cookie is None:
        return

    print("\nОсобиста інформація про студента:\n")
    filter_profile = {
        "surname": None,
        "name": None,
        "patronymic": None,
        "birthday": None,
        "sex": None,
        "image": None
    }
    get_info(url=ksu_24_profile, cookie=cookie, filter_by=filter_profile)

    print("Загальна інформація про студента:\n")
    filter_student = {
        "grade_display": None,
        "education_form_display": None,
        "funding_form_display": None,
        "speciality_code": None,
        "speciality_name": None,
        "speciality_group_name": None
    }
    get_info(url=ksu_24_student, cookie=cookie, filter_by=filter_student)
    student_id = get_value(url=ksu_24_student, cookie=cookie, key="id")

    recordbooks_url = f"{ksu_24_student}{student_id}/recordbooks/"
    get_info(url=recordbooks_url, cookie=cookie)
    recordbook_id = get_value(url=recordbooks_url, cookie=cookie, key="id")

    print("Запит на отримання інформації про дисципліни\n")
    records_url = f"{recordbooks_url}{recordbook_id}/records"
    filter_records = {
        "discipline_name": None,
        "credits": None,
        "teacher_name": None,
        "semester": None,
        "control_display": None,
        "result": None,
        "result_ects": None
    }
    response = requests.get(url=records_url, cookies={"JWT": cookie})
    response.raise_for_status()
    data = response.json().get("results", [])
    get_info(url=records_url, cookie=cookie, filter_by=filter_records)

    #Розрахунок середнього балу по семестру
    semester_results = [item for item in data if item.get("result") is not None]
    semester_average = calculate_average(semester_results, "result")
    print(f"Середній бал по семестру: {semester_average}")

    #Розрахунок середнього балу за весь час
    overall_results = [item for item in data if item.get("result") is not None]
    overall_average = calculate_average(overall_results, "result")
    print(f"Середній бал за весь час: {overall_average}")

if __name__ == "__main__":
    main()