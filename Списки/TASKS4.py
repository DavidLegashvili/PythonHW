list = []
name_list = []
surname_list = []
job_list = []
students_list = []
while True:
    name = input("Введите имя преподавателя (Для завершения введите off):")
    if name != "off":
        name_list.append(name)
        surname = input("Введите фамилию преподавателя:")
        surname_list.append(surname)
        job = input("Введите должность:")
        job_list.append(job)
        students = input("Введите количество студентов:")
        students_list.append(students)
    else:
        break
list.extend(name_list)
list.extend(surname_list)
list.extend(job_list)
list.extend(students_list)
print(list)