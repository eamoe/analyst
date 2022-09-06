# Задание 6 Напишите программу, в которой пользователь будет задавать две строки,
# а программа - определять количество вхождений одной строки в другой.
# Пример: "abababb" и "aba" -> 2

def count_substrings(main_string, substring):
      counter = 0
      for pos in range(len(main_string) - len(substring) + 1):
           if main_string[pos:pos + len(substring)] == substring:
                counter += 1
      return counter

initial_str = input("Введите строку: ")
sub_str = input("Введите подстроку: ")

print(count_substrings(initial_str, sub_str))
