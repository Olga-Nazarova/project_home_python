# Дана последовательность чисел. Получить список неповторяющихся элементов исходной последовательности
# Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [1, 2, 3, 5, 10]
lst = [12, 2, 2, 1, 13, 13, 4, 1, 5, 3, 17]
print(f'Входные данные: {lst}')
lst1 = []
count = 0
for i in lst:
	if i not in lst1:
		lst1.append(i)
print(f'Уникальные элементы: {lst1}')





