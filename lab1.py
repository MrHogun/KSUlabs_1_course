def add_numbers(num1, num2):
    return num1 + num2


def subtract_numbers(num1, num2):
    return num1 - num2


num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))

summa = add_numbers(num1, num2)
diff = subtract_numbers(num1, num2)

print("Сумма чисел:", summa)
print("Разность чисел:", diff)
