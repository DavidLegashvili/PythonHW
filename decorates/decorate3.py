"""
Напишите функцию которая принимает 2 числа и выводит все числа между ними которые делятся на 3.
Напишите декоратор который выводит фразу:
"Данная функция выводит все числа между Число А и Число Б"(сюда подставьте числа что принимает функция)
и оберните функцию чтобы данная фраза выводилась перед ее выполнением
"""

a = 12
b = 89


def func(a, b):
    functia(a, b)
    for i in range(a, b):
        if i % 3 == 0:
            print(i)


def functia(a, b):
    print(f"Данная функция выводит все числа между {a} и {b}")

decor = func(a, b)
decor()