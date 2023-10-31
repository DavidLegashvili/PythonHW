#Minigame
from random import randint

while True:
    list_comp = []
    amount = int(input("Введите сложность от 1 до 5 (Кол-во попыток):"))

    while True:
        list_comp.clear()
        first = randint(0, 9)
        list_comp.append(first)

        second = randint(0, 9)
        list_comp.append(second)

        third = randint(0, 9)
        list_comp.append(third)

        fourth = randint(0, 9)
        list_comp.append(fourth)

        set_comp = set(list_comp)
        if len(set_comp) != len(list_comp):
            list_comp.clear()               
            first = randint(0, 9)
            list_comp.append(first)

            second = randint(0, 9)
            list_comp.append(second)

            third = randint(0, 9)
            list_comp.append(third)

            fourth = randint(0, 9)
            list_comp.append(fourth)
        elif len(set_comp) == len(list_comp):
            break


    preview = int(input("1. Вывести список\n2. Не выводить список"))
    if preview == 1:
        print(list_comp)

    resultat = 0
    while True:
        print("Попробуйте угадать порядок:")
        list_correct = []
        fst = int(input("Первое число:"))
        if fst == list_comp[0]:
                list_correct.append(fst)
        elif fst in list_comp and fst != list_comp[0]:
            list_correct.append("+-")
        elif fst not in list_comp:
                list_correct.append("-")


        scd = int(input("Второе число:"))
        if scd == list_comp[1]:
                list_correct.append(scd)
        elif scd in list_comp and scd != list_comp[1]:
            list_correct.append("+-")
        elif scd not in list_comp:
                list_correct.append("-")


        thrd = int(input("Третье число:"))
        if thrd == list_comp[2]:
            list_correct.append(thrd)
        elif thrd in list_comp and thrd != list_comp[2]:
            list_correct.append("+-")
        elif thrd not in list_comp:
                list_correct.append("-")


        frth = int(input("Четвертое число:"))
        if frth == list_comp[3]:
            list_correct.append(frth)
        elif frth in list_comp and frth != list_comp[3]:
            list_correct.append("+-")
        elif frth not in list_comp:
                list_correct.append("-")

        resultat += 1

        print(list_correct)
        if list_correct == list_comp:
            print("Вы угадали!")
            print("--------------- ИГРА ОКОНЧЕНА ---------------")
            break

        if resultat == amount:
            print("--------------- ИГРА ОКОНЧЕНА ---------------")
            print(f"Изначальный список был: {list_comp}")
            list_correct.clear()
            break
    wants = input("Хотите попробовать снова?\n1.Да\n2.Нет").lower()
    if wants == "нет" or wants == "2":
         break











