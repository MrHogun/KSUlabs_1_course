import datetime
import json
import csv

#Створення класу
class Person:
    name: str = None
    birthday: datetime.date = None

    def __init__(self, name: str, birthday: str):
        self.name = name
        self.birthday = datetime.datetime.fromisoformat(birthday).date()

    def __str__(self):
        return f"{self.name} [{self.birthday}]"

    def __eq__(self, other):
        return self.birthday == other.birthday and self.name == other.name

    def __lt__(self, other):
        if self.birthday != other.birthday:
            return self.birthday < other.birthday
        else:
            return self.name < other.name

    def __gt__(self, other):
        if self.birthday != other.birthday:
            return self.birthday > other.birthday
        else:
            return self.name > other.name

    def to_dict(self):
        return {
            'name': self.name,
            'birthday': self.birthday.isoformat(),
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data['name'], data['birthday'])

    @staticmethod
    def from_csv_row(row):
        return Person(row['name'], row['birthday'])

    def to_csv_row(self):
        return {'name': self.name, 'birthday': self.birthday.isoformat()}


#Перша та друга колекції людей
people1 = [
    Person("Andrey", "2005-03-28"),
    Person("Peter", "2000-12-09"),
    Person("Roman", "2008-02-25"),
    Person("Aleksandr", "2006-01-12"),
    Person("Daniil", "1999-05-17")
]

people2 = [
    Person("Dmitry", "2005-03-02"),
    Person("Yevgeny", "2008-05-01"),
    Person("Vadim", "2004-01-21"),
    Person("Sergey", "2004-05-27"),
    Person("Nikita", "2002-05-06")
]

#Збереження першої колекції людей у форматі JSON
json_data = [person.to_dict() for person in people1]
with open("people.json", "w") as json_file:
    json.dump(json_data, json_file, indent=4)

#Зчитування першої колекції людей у форматі JSON
with open("people.json", "r") as json_file:
    json_data = json.load(json_file)
    people_from_json = [Person.from_dict(data) for data in json_data]

print("\nПерша колекція людей зчитана зі збереженного JSON:")
for person in people_from_json:
    print(person)

#Збереження другої колекції люей у форматі CSV
with open("people.csv", "w", newline='') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=['name', 'birthday'])
    writer.writeheader()
    writer.writerows([person.to_csv_row() for person in people2])

#Зчитування другої колекції людей у форматі CSV
with open("people.csv", "r") as csv_file:
    reader = csv.DictReader(csv_file)
    people_from_csv = [Person.from_csv_row(row) for row in reader]

print("\nДруга колекція лдей зчитана зі збереженного CSV:")
for person in people_from_csv:
    print(person)