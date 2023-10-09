"""
Каждый стажёр мог выбрать любое число предметов для изучения. По каждому предмету он мог набрать от 0 до 50 баллов.

Программа должна:
Пока пользователь не введет "стоп"":
1. Запрашивать имя студента и число предметов.
2. Запрашивать число баллов по каждому предмету и печатать общую сумму баллов: «Итоговый счёт: _».
3. По сумме баллов опеределять тип грамоты о прохождении стажировки:
- баллов больше 80 — «Наградить дипломом.»;
- баллов больше 50 и меньше или равно 80 — «Наградить похвальной грамотой.»;
- остальные случаи — «Выдать грамоту об участии.».
"""

def students(name, amount, points, sum):
    sum = sum(points_list[0])  // sum(amount_list[0])
    sum1 = sum(points_list[1])  // sum(amount_list[1]) 
    sum2 = sum(points_list[2])  // sum(amount_list[2]) 
    sum3 = sum(points_list[3])  // sum(amount_list[3])
    sum4 = sum(points_list[4])  // sum(amount_list[0])
    for i in sum, sum1, sum2, sum3, sum4, name:
        if i > 79:
              print("Наградить дипломом", name[i])
        elif i > 49:
              print("Наградить похвальной грамотой")
        else:
             print("Выдать грамоту об участии")





amount_list = []
points_list = []
print("Вводить можно максимум 5 студентов")
while True:
        amount = int(input("Введите общее число предметов:"))
        amount_list.append(amount)
        for i in range(amount):
             points = int(input("Введите количество баллов за предмет:"))
             points_list.append(points)             
             name = input("Введите имя:").lower()
             break

students(amount_list, points_list, name)