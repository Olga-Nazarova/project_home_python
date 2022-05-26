import _locale
_locale._getdefaultlocale = (lambda *args: ['en_US', 'utf8'])

num = 3
file = open('guide.cvs', 'w')
for i in range(num):
    surname = input('Фамилия: ')
    name = input('Имя: ')
    phone_number = input('Номер телефона: ')
    comment = input('Описание: ')
    file.write(f'{surname}\n{name}\n{phone_number}\n{comment}\n \n')
file.close()

file2 = open('guide2.cvs', 'w')
file2.write(f'{surname}, {name}, {phone_number}, {comment}\n'
            f'{surname}, {name}, {phone_number}, {comment}\n'
            f'{surname}, {name}, {phone_number}, {comment}\n')
file2.close()