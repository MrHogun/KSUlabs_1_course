import datetime

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

#Сортування двох колекцій людей за датою народження
people1.sort()
people2.sort()

print("Колекція 1 відсортована за датою народження:")
for person in people1:
    print(person)

print("\nКолекція 2 відсортована за датою народження:")
for person in people2:
    print(person)

#Сортування двох колекцій людей за ім'ям
people1.sort(key=lambda x: x.name)
people2.sort(key=lambda x: x.name)

print("\n\nКолекція 1 відсортована за ім'ям:")
for person in people1:
    print(person)

print("\nКолекція 2 відсортована за ім'ям:")
for person in people2:
    print(person)

#Порівняння двох колекцій людей на ідентичність
if people1 == people2:
    print("\n\nКолекції однакові.")
else:
    print("\n\nКолекції не однакові")