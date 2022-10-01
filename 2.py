N = int(input("Введите число N: "))

set_of_multiplication = []
count = 1
for i in range(N):
    count *= i + 1
    set_of_multiplication.append(count)
print(f"Набор произведений числа N = {set_of_multiplication}")
