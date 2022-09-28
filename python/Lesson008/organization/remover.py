import reader
import constants

def delete_item(file_name):
    path = constants.folder + file_name + '.csv'
    return delete(path, file_name)


def delete(path, file_name):
    if file_name == "departments":
        reader.read_departments(path)
    if file_name == "salaries":
        reader.read_salaries(path)
    if file_name == "employees":
        reader.read_employees(path)
    dept_id = input("\n\nУкажите ID удаляемой записи: ")
    is_found = False
    with open(path, "r") as file:
        lines = file.readlines()
    with open(path, "w") as file:
        for line in lines:
            line_list = line.split(";")
            if line_list[0] == dept_id:
                is_found = True
                pass
            else:
                file.write(line)
    if is_found == True:
        output_str = f"Запись с кодом {dept_id} удалена!"
    else:
        output_str = f"Запись не найдена!"
    return output_str
