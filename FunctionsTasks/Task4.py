"""
Напишите программу считающую и обрабатывающую индекс массы тела.
В одной функции программа должна считать ИМТ. В другой обрабатывать, если ИМТ ниже 18.5 печатать "Недостаточный вес",
от 18.5 до 25 "ИМТ в норме", больше 25 "Избыточный вес".
Формула определения ИМТ: index = weight / (height * height)
"""
weight = int(input("Введите вес:"))
height = int(input("Введите рост:"))

def IMT (weight, height):
    imt = weight / height ** 2
    return imt

def areyoufatorno (imt):
    if imt < 18.5:
        print("You are skinny")
    elif imt in range(18.5, 26):
        print("You are fine")
    elif imt > 26:
        print("You are fat:(")

        