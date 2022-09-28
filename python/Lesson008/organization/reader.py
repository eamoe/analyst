import constants

dept_header     = "   ID   |       Created        |        Updated        |     Name     "
salaries_header = "   ID   |       Created        |        Updated        |  Amount  "

def show_items(file_name):
    path = constants.folder + file_name + '.csv'
    if file_name == "departments":
        print(dept_header)
        read_departments(path)
    if file_name == "salaries":
        print(salaries_header)
        read_salaries(path)
    if file_name == "employees":
        read_employees(path)


def read_departments(path):
    data = open(path, 'r')
    for line in data:
        line = line.replace("\n", "")
        list_items = line.split(';')
        print(f"  {list_items[0]} | {list_items[2]}  | {list_items[3]}   |  {list_items[1]}  ")
    data.close()


def read_salaries(path):
    data = open(path, 'r')
    for line in data:
        line = line.replace("\n", "")
        list_items = line.split(';')
        print(f"  {list_items[0]} | {list_items[2]}  | {list_items[3]}   |  {list_items[1]}  ")
    data.close()


def read_employees(path):
    data = open(path, 'r')
    for line in data:
        line = line.replace("\n", "")
        list_items = line.split(';')
        print(f"ID: {list_items[0]}")
        print(f"Фамилия: {list_items[1]}")
        print(f"Имя: {list_items[2]}")
        print(f"Отчество: {list_items[3]}")
        print(f"Отдел: {get_dept_name(list_items[4])}")
        print(f"Оклад: {get_salary_amount(list_items[5])}")
        print(f"Дата создания: {list_items[6]}")
        print(f"Дата обновления: {list_items[7]}")
        print("\n")
    data.close()


def get_dept_name(dept_id):
    dept_name = f"запись {dept_id} не найдена"
    path = constants.folder + "departments" + '.csv'
    data = open(path, 'r')
    for line in data:
        line = line.replace("\n", "")
        list_items = line.split(';')
        if list_items[0] == dept_id:
            dept_name = list_items[1]
    data.close()
    return dept_name


def get_salary_amount(salary_id):
    dept_name = f"запись {salary_id} не найдена"
    path = constants.folder + "salaries" + '.csv'
    data = open(path, 'r')
    for line in data:
        line = line.replace("\n", "")
        list_items = line.split(';')
        if list_items[0] == salary_id:
            dept_name = list_items[1]
    data.close()
    return dept_name