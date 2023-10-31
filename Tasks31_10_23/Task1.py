#1.	Напишите программу, запрашивающую у пользователя общий список студентов в группе и список студентов
#отсутствующих на занятии. Программа должна выводить сначала общий список, потом список присутствующих на занятии 
#и после список отсутствующих.


list_students = []
list_missed_students = []
students_at_class = []

while True:
    students = input("Введите имя студента:")
    if students != "off":
        list_students.append(students)
        students_at_class.append(students)
    elif students == "off":
        break

while True:
    missed_students = input("Введите отсутствующих:")
    if missed_students != "off":
        list_missed_students.append(missed_students)
    elif missed_students == "off":
        break

for i in list_students:
    if i in list_missed_students:
        students_at_class.remove(i)


print(f"Список студентов: {list_students}\nСписок присутствующих: {students_at_class}\nСписок отсутствующих: {list_missed_students}")
