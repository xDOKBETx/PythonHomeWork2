number = input("Введите число: ")
sum = 0
for i in number:
    if i.isdigit():
        sum += int(i)
print("Сумма цифр числа равна:", sum)
