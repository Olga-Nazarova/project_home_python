def choice():
    selector = None
    try:
        selector = int(input('Введите "1" если хотите добавить новый контакт\n' + \
                             'Введите "2" если хотите найти контакт\n' + \
                             'Введите "3" если хотите удалить контакт\n' + \
                             'Введите "4" если хотите просмотреть всю адресную книгу\n' + \
                             'Введите "5" если хотите завершить работу\n' + \
                             '\n'))
    except ValueError:
        print('\n Не корректный ввод! Повторите: \n')
    return selector

def add_member():
    surname = input("Введите фамилию: ").capitalize()
    name = input("Введите имя: ").capitalize()
    phone_number = input("Введите номер телефона: ").capitalize()
    comment = input("Введите описание: ").capitalize()
    file = open('guide.cvs', 'a')
    file.write('{0:10}\n{1:10}\n{2}\n{3}\n'.format(surname, name, phone_number, comment) + '\n')
    print('\nКонтакт {lastName} {name} успешно добавлен\n'.format(lastName=surname, name=name))
    file.close()

def find_member():
    surname = input("Введите фамилию для поиска: ").capitalize()
    file = open('guide.cvs')
    content = file.readlines()
    count = 0
    while (count != len(content)):
        if content[count].strip() == surname.strip():
            print(content[count] + content[count + 1] + content[count + 2] + content[count + 3])
        count += 1
    file.close()

def print_all():
    file = open('guide.cvs')
    content = file.readlines()
    basic = []
    for i in content:
        if i == '\n':
            print('')
            basic = list(filter(None, basic))
            print(*basic, sep=',', end="")
            basic = []
        basic.append(i.strip())
    print("\n")
    file.close()

def delete_string(string_num):
    delete_item = int(string_num)
    with open("guide.cvs", "r+") as f:
        content = f.readlines()
        f.seek(0)
        count: int = 0
        while (count != len(content)):
           if (count != delete_item) and count != delete_item + 1 and count != delete_item + 2 and \
                   count != delete_item + 3 and count != delete_item + 4:
               f.write(content[count])
           count += 1
        f.truncate()

def remove_member():
    surname = input("Введите фамилию для удаления контакта: ").capitalize()
    file = open('guide.cvs')
    content = file.readlines()
    count = 0
    while (count != len(content)):
        if content[count].strip() == surname.strip():
            delete_string(count)
            break
        count += 1
    file.close()
    print('Контакт полностью удалён')


while True:
    selector = choice()
    if selector == 1:
        print("Выбрано добавить новый контакт")
        add_member()
    elif selector == 2:
        print("Выбрано найти контакт")
        find_member()
    elif selector == 3:
        print("Выбрано удалить контакт")
        remove_member()
    elif selector == 4:
        print("Выбрано посмотреть все контакты")
        print_all()
    elif selector == 5:
        print("Вы вышли из программы. Спасибо и до скорых встреч!")
        break