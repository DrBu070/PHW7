def get_info ():
    info = []
    surname = input('Введите Фамилию: ')
    info.append(surname)
    name = input('Введите Имя: ')
    info.append(name)
    phone_number = ''
    valid =False
    while not valid:
        try:
            phone_number = input('Введите номер телефона после +7: ')
            if len(phone_number) != 10:
                print('В номере телефона должно быть 10 цифр.')
            else:
                phone_number = int(phone_number)
                valid = True
        except:
            print('Номер телефона должен содержать только цыфры!')
    info.append(phone_number)
    description = input('Введите описание: ')
    info.append(description)
    return info
from Interface import get_info as gi
