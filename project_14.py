# Подсчитать сумму цифр в вещественном числе.
n =input('Введите число: ')
length = len(n)
n = int(n)
s = 0
for i in range(length):
    s = s + (n %10)
    n=n//10
    i += i
print(s)



# 2 вариант
print(sum(map(int, input('Введите трехзначное число: ').replace('.',""))))
