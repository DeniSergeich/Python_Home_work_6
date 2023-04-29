array = input("Введите массив чисел через пробел: ").split()
min_value = int(input("Введите минимальное значение: "))
max_value = int(input("Введите максимальное значение: "))

result = []
for i, elem in enumerate(array):
    if min_value <= int(elem) <= max_value:
        result.append(i)

print(result)