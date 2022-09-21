# Задача: предложить улучшения кода для уже решённых задач (4 задачи из любых семинаров, кроме первого):
# С помощью использования лямбд, filter, map, zip, enumerate, list comprehension
# В ответе должны присутствовать старые и новые варианты решений.


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

print(f"(OLD) Количество вхождений: {count_substrings(initial_str, sub_str)}")


# Новое решение
def count_substrings_new(in_str, sub_str):
      in_len = len(in_str)
      sub_len = len(sub_str)
      stop = in_len - sub_len + 1
      occurences = [i for i in range(stop) if in_str[i : i + sub_len] == sub_str]
      return len(occurences)


print(f"(NEW) Количество вхождений: {count_substrings_new(initial_str, sub_str)}")
