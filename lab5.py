import requests

#Фуек-я логіну користувача
def authentication(login: str, password: str):
    response = requests.post("https://ksu24.kspu.edu/api/v2/login/",
                             data={'username': login, 'password': password})
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

#Функ-я отримання значень результатія запиту через API
def get_value(url: str, cookie: str, key: str, filter_by: dict = None):
    response = requests.get(url=url, cookies={'JWT': cookie})
    response.raise_for_status()

    data = response.json()
    for item in data.get('results', [data]):
        if filter_by and item.get(list(filter_by.keys())[0]) != filter_by.get(list(filter_by.keys())[0]):
            continue
        if key in item:
            return item[key]
    if filter_by is None:
        print("This key doesn't exist...")
    else:
        print("No information found for the specified filter...")
    return None

#Функ-я отримання інформації з API
def get_info(url: str, cookie: str):
    response = requests.get(url=url, cookies={'JWT': cookie})
    response.raise_for_status()

    data = response.json()
    results_list = data.get('results', [data])
    for dictionary in results_list:
        for key, value in dictionary.items():
            print(f"{key}: {value}")
        print("-" * 30)

def main():
    ksu_24_student = "https://ksu24.kspu.edu/api/v2/my/students/"
    ksu_24_profile = "https://ksu24.kspu.edu/api/v2/my/profile/"
    login = input("Введіть ваш логін: ")
    password = input("Введіть ваш пароль: ")
#Запит на логін\пароль
    cookie = authentication(login=login, password=password)
    if cookie is None:
        return

    print("\nОсобиста інформація про студента:\n")
    get_info(url=ksu_24_profile, cookie=cookie)

    print("Загальна інформація про студента:\n")
    get_info(url=ksu_24_student, cookie=cookie)
    student_id = get_value(url=ksu_24_student, cookie=cookie, key="id")

    print("Запит на отримання оцінок \n")
    recordbooks_url = f"{ksu_24_student}{student_id}/recordbooks/"
    get_info(url=recordbooks_url, cookie=cookie)
    recordbook_id = get_value(url=recordbooks_url, cookie=cookie, key="id")

    print("Запит на отримання інформації про дисципліни\n")
    records_url = f"{recordbooks_url}{recordbook_id}/records"
    get_info(url=records_url, cookie=cookie)

if __name__ == "__main__":
    main()