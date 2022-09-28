import reader
from datetime import datetime as dt
import constants

def update_item(file_name):
    path = constants.folder + file_name + '.csv'
    if file_name == "departments":
        return update_department(path)
    if file_name == "salaries":
        return update_salary(path)
    if file_name == "employees":
        return update_employee(path)


def update_department(path):
    reader.read_departments(path)
    dept_id = input("\n\nУкажите ID изменяемой записи: ")
    is_found = False
    with open(path, "r") as file:
        lines = file.readlines()
    with open(path, "w") as file:
        for line in lines:
                line = line.strip("\n")
                line_list = line.split(";")
                if line_list[0] == dept_id.lower():
                    is_found = True
                    new_dept_id = line_list[0]
                    new_dept_name = input("Введите название отдела: ")
                    if new_dept_name == "":
                        new_dept_name = line_list[1]
                    new_created = line_list[2]
                    new_updated = str(dt.now().date()) + ' ' + str(dt.now().strftime('%H:%M:%S'))
                    file.write('{};{};{};{}\n'
                        .format(new_dept_id, new_dept_name, new_created, new_updated))
                else:
                    file.write(line + "\n")
    if is_found == True:
        output_str = f"Запись с кодом {dept_id} обновлена!"
    else:
        output_str = f"Запись не найдена!"
    return output_str


def update_salary(path):
    reader.read_salaries(path)
    salary_id = input("\n\nУкажите ID изменяемой записи: ")
    is_found = False
    with open(path, "r") as file:
        lines = file.readlines()
    with open(path, "w") as file:
        for line in lines:
                line = line.strip("\n")
                line_list = line.split(";")
                if line_list[0] == salary_id.lower():
                    is_found = True
                    new_salary_id = line_list[0]
                    new_amount = float(input("Укажите новый размер оклада: "))
                    if new_amount == "":
                        new_amount = line_list[1]
                    new_created = line_list[2]
                    new_updated = str(dt.now().date()) + ' ' + str(dt.now().strftime('%H:%M:%S'))
                    file.write('{};{};{};{}\n'
                        .format(new_salary_id, new_amount, new_created, new_updated))
                else:
                    file.write(line + "\n")
    if is_found == True:
        output_str = f"Запись с кодом {salary_id} обновлена!"
    else:
        output_str = f"Запись не найдена!"
    return output_str


def update_employee(path):
    reader.read_employees(path)
    employee_id = input("\n\nУкажите ID изменяемой записи: ")
    is_found = False
    with open(path, "r") as file:
        lines = file.readlines()
    with open(path, "w") as file:
        for line in lines:
                line = line.strip("\n")
                line_list = line.split(";")
                if line_list[0] == employee_id.lower():
                    is_found = True
                    new_employee_id = line_list[0]
                    new_last_name = input("Фамилия: ")
                    if new_last_name == "":
                        new_last_name = line_list[1]
                    new_first_name = input("Имя: ")
                    if new_first_name == "":
                        new_first_name = line_list[2]
                    new_middle_name = input("Отчество: ")
                    if new_middle_name == "":
                        new_middle_name = line_list[3]
                    print("\nСписок департаментов".upper())
                    reader.show_items("departments")
                    new_dept_id = input("Код департамента: ")
                    if new_dept_id == "":
                        new_dept_id = line_list[4]
                    print("\nСписок окладов".upper())
                    reader.show_items("salaries")
                    new_salary_id = input("Код оклада: ")
                    if new_salary_id == "":
                        new_salary_id = line_list[5]
                    new_created = line_list[6]
                    new_updated = str(dt.now().date()) + ' ' + str(dt.now().strftime('%H:%M:%S'))
                    file.write('{};{};{};{};{};{};{};{}\n'
                        .format(new_employee_id, new_last_name, new_first_name, new_middle_name, new_dept_id, new_salary_id, new_created, new_updated))
                else:
                    file.write(line + "\n")
    if is_found == True:
        output_str = f"Запись с кодом {employee_id} обновлена!"
    else:
        output_str = f"Запись не найдена!"
    return output_str
