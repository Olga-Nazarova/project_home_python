# Реализовать алгоритм перемешивания списка.
import random
test_list = [1, 4, 5, 6, 3]
print ("Оригинал : " + str(test_list))
for i in range(len(test_list)-1, 0, -1):
    j = random.randint(0, i + 1)
    test_list[i], test_list[j] = test_list[j], test_list[i]
print ("Перетасовка : " +  str(test_list))



# 2  вариант

import random
lst = [random.randint(5,15) for i in range(random.randint(10,20))]
print(f"Исходный список:\n {lst}")
random.shuffle(lst)
print(f"Список после перемешивания:\n{lst}")