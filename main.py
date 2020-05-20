from brut_logins import login_by_name_and_second_name, login_by_name, login_by_email, login_by_math

# функция быстрого перебора (предполагаемые логин и пароль, зная имя, дату рождения и пр)
# добавить функцию перебора логина через базу популярных логинов
# (ТЗ в ДЗ ломать определённого человека, так что  реализую позже)
# запуск через функции
# TO DO: добавить перебор логинов и паролей  по "ключевым" словам:
# марка машины, увлечения спортом, город\улица проживания и т.д.
def quick_runner():
    full_succsec = login_by_name_and_second_name()
    if full_succsec != None:
        print(full_succsec)
        return


    full_succsec = login_by_email()
    if full_succsec != None:
        print(full_succsec)
        return


    full_succsec = login_by_name()
    if full_succsec != None:
        print(full_succsec)
        return




# функция "математического брута" - перебирая все возможные логины\пароли из алфавитов.
# сами алфавиты разнесены по разным переменным
# TO DO: расширить алфавит логинов до всех символов, исключая спецсимволы, т.к. обычно в логинах запрещены
# TO DO: расширить алфавит паролей до всех символов, включая спецсимволы

def long_runner():
    full_succsec = login_by_math()
    if full_succsec != None:
        print(full_succsec)
        return

# запуск перебора разделён на быстрый и полный(долгий)
# при необходимости запускаем быстрый несколько раз, меняя входные данные (например Д.Р может быть формата YYYY или YY)
# это так же упрощает модификацию подборов;
# TO DO: добавить в long_runner() вариации предполагаемых логинов с математическим подбором паролей

quick_runner()
long_runner()





