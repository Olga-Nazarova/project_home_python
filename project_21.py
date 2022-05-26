#Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.
#Примеры
#список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
#список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
#список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
#список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
#список: [], ищем: "123", ответ: -1


def search_two(lines, query):
    count = 0
    result = 0
    while (result != 2 and count < len(lines)):
        if lines[count] == query:
            result += 1
        count += 1
    print("-1") if result < 2 else print(count - 1)

lines1 = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
lines2 = ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"]
lines3 = ["йцу", "фыв", "ячс", "цук", "йцукен"]
lines4 = ["123", "234", 123, "567"]
query1 = "qwe"
query2 = "йцу"
query3 = "йцу"
query4 = "123"

search_two(lines1, query1)
search_two(lines2, query2)
search_two(lines3, query3)
search_two(lines4, query4)