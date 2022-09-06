# Задание 5 Реализуйте алгоритм перемешивания списка.

import random

numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def shuffle(numbers):
    for n in range(len(numbers) - 1, 0, -1):
        index = random.randint(0, n + 1)
        temp = numbers[n]
        numbers[n] = numbers[index]
        numbers[index] = temp
    return numbers
	
print ("Исходный список : " + str(numbers_list))
print ("Перемешанный список : " + str(shuffle(numbers_list)))
