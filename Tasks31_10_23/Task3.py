#3.	Создайте список имен(не меньше 5).Напишите функцию которая принимает список и с периодичностью в 0.5 
#секунды записывает в файл числа от 0 до 100 с шагом 3 + Имя из списка выбранное случайно.

import random
import time

list_names = ["david", "lera", "arina", "dasha", "nikita", "ivan"]

with open("names.txt", "w+") as file:
    for i in range(100):
        file.write(())
    time.sleep(0.5)
    file.write((0 + 3) + random.choice(list_names))

    #skip
