# Задать список из n чисел последовательности (1+1n)^n и вывести на экран их сумму
x = int(input('Введите количество членов последовательности: '))
print(sum([(1+1*n)**n for n in range(1, x+1)]))


# 2 вариант

lst = [(1+1/i)**i for i in range(1,n+1)]
print(f"Полученная сумма последовательности (1+1/n)^n равнна {round(sum(lst),2)}")