"""
2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.

Пример:
Иван Иванов 1846 года рождения, проживает в городе Москва,
email: jackie@gmail.com, телефон: 01005321456
"""


def person_info(name, surname, birth_year, birth_city, current_city, email, number):
    print(f"{name.capitalize()} {surname.capitalize()} {birth_year} г.р, "
          f"родился в г. {birth_city.capitalize()}, сейчас проживает в г. "
          f"{current_city.capitalize()},\n{email =}, телефон: {number}")


person_info(name='ivan', surname='petrov', number='8-977-301-82-40', email='keks@mail.ru',
            current_city='moscow', birth_city='dushanbe', birth_year=1986)
