# # Даны два файла в каждом из которых находится запись многочлена.
# Сформировать файл содержащий сумму многочленов.
one_file = open('task_34_1.txt', 'w')
two_file = open('task_34_2.txt', 'w')
example_1 = '2 * x ^ 2 + 21 * x ^ 6 + 24 = 0'
example_2 = '34 * x ^ 2 + 48 * x ^ 6 + 23 = 0'
one_file.write(example_1)
two_file.write(example_2)
one_file.close()
two_file.close()
#Создали два файла с уравнениями многочленов

file1 = open('task_34_1.txt', 'r')
file2 = open('task_34_2.txt', 'r')
strone = file1.readline()
strtwo = file2.readline()

resmass = []
polynom = ''


def splitter(str):
    str = str.replace(' ', '')
    mass = str.split('+')
    return mass


def createnum(mass):
    resmass = []
    for i in range(0, len(mass)):
        linex = ''
        line = mass[i]
        for i in range(0, len(line)):
            if line[i].isdecimal():
                linex += line[i]
            else:
                break
        resmass.append(linex)
    return resmass


def notequal(arr1, arr2):
    diff = (len(arr1) - len(arr2))
    for i in range(0, len(arr1)):
        if diff > 0:
            resmass.append(int(arr1[i]))
        else:
            resmass.append(int(arr1[i]) + int(arr2[-diff]))
        diff -= 1
    return resmass


massone = splitter(strone)
masstwo = splitter(strtwo)
massonefin = createnum(massone)
masstwofin = createnum(masstwo)

if len(massonefin) == len(masstwofin):
    for i in range(0, len(massonefin)):
        resmass.append(int(massonefin[i]) + int(masstwofin[i]))
elif len(massonefin) > len(masstwofin):
    resmass = notequal(massonefin, masstwofin)
elif len(massonefin) < len(masstwofin):
    resmass = notequal(masstwofin, massonefin)

for i in range(len(resmass) - 1, -1, -1):
    if i > 1:
        polynom += str(resmass[-(i + 1)]) + ' * x ^ ' + str(i) + ' + '
    elif i == 1:
        polynom += str(resmass[-(i + 1)]) + ' * x + '
    elif i == 0:
        polynom += str(resmass[-(i + 1)]) + ' = 0'

endpoly = open('task_34_3.txt', 'w')
endpoly.write(polynom)
print(massonefin)
print(masstwofin)
print(polynom)
endpoly.close()
