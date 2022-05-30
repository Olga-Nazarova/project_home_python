#Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15]

def compose(numbers):
    result = []
    while (len(numbers) != 0):
        if len(numbers) == 1:
            result.append(numbers[0] * numbers[0])
            numbers.pop(0)
        else:
            result.append(numbers[0] * numbers[-1])
            numbers.pop(0)
            numbers.pop(-1)
    print(result)

numbers = [2, 3, 4, 5, 6]
numbers2 = [2, 3, 5, 6]

compose(numbers)
compose(numbers2)