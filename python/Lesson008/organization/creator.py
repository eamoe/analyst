from asyncio import constants
from unique_id import *
from datetime import datetime as dt
import reader
import constants

def generate_id():
    return get_unique_id(length = 5,
                        excluded_chars="{%!#}*->$;@~:&,^_<[]`=/'\?.()|+\"")


def create_item(file_name):
    path = constants.folder + file_name + '.csv'
    if file_name == "departments":
        return create_department(path)
    elif file_name == "salaries":
        return create_salary(path)
    elif file_name == "employees":
        return create_employee(path)


def create_department(path):
    print("Cоздание департамента".upper())
    dept_id = generate_id().lower()
    dept_name = input("Введите название: ")
    created = str(dt.now().date()) + ' ' + str(dt.now().strftime('%H:%M:%S'))
    updated = str(dt.now().date()) + ' ' + str(dt.now().strftime('%H:%M:%S'))
    with open(path, 'a') as file:
        file.write('{};{};{};{}\n'
                    .format(dept_id, dept_name, created, updated))
    return f"Создан департамент:\n\nID = {dept_id}\nНаименование = {dept_name}\n"


def create_salary(path):
    print("Cоздание оклада".upper())
    salary_id = generate_id().lower()
    is_correct = False
    while not is_correct:
        try:
            salary = float(input("Введите сумму: "))
            is_correct = True
        except:
            print("Некорректное значение!")
    created = str(dt.now().date()) + ' ' + str(dt.now().strftime('%H:%M:%S'))
    updated = str(dt.now().date()) + ' ' + str(dt.now().strftime('%H:%M:%S'))
    with open(path, 'a') as file:
        file.write('{};{};{};{}\n'
                    .format(salary_id, salary, created, updated))
    return f"Создана новая запись в справочнике зарплат:\n\nID = {salary_id}\nСумма = {salary}\n"


def create_employee(path):
    print("Добавление сотрудника".upper())
    employee_id = generate_id().lower()
    last_name = input("Фамилия: ")
    first_name = input("Имя: ")
    middle_name = input("Отчество: ")
    print("\nСписок департаментов".upper())
    reader.show_items("departments")
    department_id = input("Введите код департамента: ")
    print("\nСписок окладов".upper())
    reader.show_items("salaries")
    salary_id = input("Введите код оклада: ")
    created = str(dt.now().date()) + ' ' + str(dt.now().strftime('%H:%M:%S'))
    updated = str(dt.now().date()) + ' ' + str(dt.now().strftime('%H:%M:%S'))
    with open(path, 'a') as file:
        file.write('{};{};{};{};{};{};{};{}\n'
                    .format(employee_id, last_name, first_name, middle_name, department_id, salary_id, created, updated))
    return f"Создана новая запись в справочнике сотрудников:\n\nID: {employee_id}\nФамилия: {last_name}\nИмя: {first_name}\nОтчество: {middle_name}\nКод департамента: {department_id}\nКод оклада: {salary_id}"
