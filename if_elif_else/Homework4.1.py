#Задача 5*: Число делится на 6 при соблюдении 2 условий:
# 1 – последняя его цифра четная
# 2 – сумма всех его чисел делится на 3
#Колхозный вариант
num = 0
num_list = []
while True:
    num = int(input("Введите число по цифрам (Для окончания введите 00):"))
    if num > 0:
        num_list.append(num)
    if num == 00:
        break
summa = sum(num_list)
last_num = num_list[-1]
number = num_list[0]
for d in num_list[1:]:
    number = 10 * number + d
if last_num // 2 == 0 and summa // 3 == 0:
    print("Ваше число делится на 6")
else:
    print("Ваше число не делится на 6")
#Тоже не работает:(((((((


