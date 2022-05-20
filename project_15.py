# Написать программу получающую набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда [ 1, 2, 6, 24 ]

n = int(input('Введите число: '))
li = [i for i in range(1,n+1)]
print(len(li))
def changed(li_n):
    count=1
    for i in range(n):
        count = li_n[i]*count
        li_n[i]=count
    return li_n
print(changed(li))


#2 Вариант
N = int(input("Введите N для набора произведений чисел от 1 до N: "))
lst = [1]
for i in range(2, N+1):
    lst.append(lst[i-2] * i)
print(f"Итоговый набор {lst}")

# 3 вариант
lst = [ lst[i-2] * i if lst[i-2] != 0 else 1 for i in range(2, N+1) ]
print(f"Итоговый набор {lst}")