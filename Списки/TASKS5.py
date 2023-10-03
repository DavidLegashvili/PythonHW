num_list = []
while True:
    num = int(input("Введите числа(Вводить до 0)"))
    if num > 0:
        num_list.append(num)
    if num == 0:
        break
if num_list.sort() == num_list:
    print("Да")
elif num_list.sort() != num_list:
    ("Нет")
elif len(num_list) == 1:
    print("Нет")
