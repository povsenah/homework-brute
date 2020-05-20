from brut_passwords import runner_bruteforsers, name, second_name, birthday, email, long_runner_bruteforsers

alphabet: str = '0123456789dog'             #   алфавит ограничен для ускорения тестирования


def login_by_name_and_second_name():        # функция перебора для возможных вариаций логинов (зная имя и пароль)
    login = name
    succses_login = runner_bruteforsers(login)
    if succses_login != None:
        return f'Логин и пароль подобраны!  \n\n {succses_login}'
    login = second_name
    succses_login = runner_bruteforsers(login)
    if succses_login != None:
        return f'Логин и пароль подобраны!  \n\n {succses_login}'
    login = name + second_name
    succses_login = runner_bruteforsers(login)
    if succses_login != None:
        return f'Логин и пароль подобраны!  \n\n {succses_login}'
    login = name[0] + second_name
    succses_login = runner_bruteforsers(login)
    if succses_login != None:
        return f'Логин и пароль подобраны!  \n\n {succses_login}'
    login = name[0] + '.' + second_name
    succses_login = runner_bruteforsers(login)
    if succses_login != None:
        return f'Логин и пароль подобраны!  \n\n {succses_login}'


def login_by_name():           #        функция перебора для возможных вариаций логинов (зная имя и Д.Р.)
    login = name + birthday
    succses_login = runner_bruteforsers(login)
    if succses_login != None:
        return f'Логин и пароль подобраны! \n\n'

    for i in range(1000):     # часто в логине имя уже занято, используют вариации с цифрами, например artem777
        login = name + str(i)
        succses_login = runner_bruteforsers(login)
        if succses_login != None:
            return f'Логин и пароль подобраны! \n\n'


#       функция перебора для возможных вариаций логинов (зная почту и Д.Р.)
def login_by_email():                               # для логигна обычно не используются спецсимволы
    login = (email.split('@')[0])                   # отсекаем всё, что после @ и её тоже
    succses_login = runner_bruteforsers(login)
    if succses_login != None:
        return f'Логин и пароль подобраны! \n\n'

    login = (email.split('@')[0]) + birthday        # Вариант логина "почта до @ + дата рождения"
    succses_login = runner_bruteforsers(login)
    if succses_login != None:
        return f'Логин и пароль подобраны! \n\n'

    # часто в логин, использующий первую часть почты, уже занят. Возможны варианты "pikabu123"@example.ru
    for i in range(1000):
        login = (email.split('@')[0]) + str(i)
        succses_login = runner_bruteforsers(login)
        if succses_login != None:
            return f'Логин и пароль подобраны! \n\n'


def login_by_math():                #   функция для полного брута (через алфавит)
    base = len(alphabet)
    i = 0
    length = 4
    while True:
        login = ''
        temp = i
        while temp != 0:
            rest = temp % base
            temp = temp // base
            login = alphabet[rest] + login

        login = '0' * (length - len(login)) + login
        succses_login = long_runner_bruteforsers(login)     # для неё используем такую же функцию подбора пароля
        if succses_login != None:
            return f'Логин и пароль подобраны! \n\n'
        if login == length * alphabet[-1]:
            length += 1
            i = 0
        else:
            i += 1
