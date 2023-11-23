#2.	Запрограммируй класс Student

class Student:
    def __init__(self, name, mid_score, course):
        self.name = name
        self.mid_score = mid_score
        self.course = course

    def whatcourse(self):
        what_course = input("Введите курс: ")
        self.course = what_course

    def info(self):
        print(f"Имя: {self.name}\nСредний балл: {self.mid_score}\nВыбранный курс: {self.course}")

    
david = Student("david", 4.1, "-")

david.whatcourse()
david.info()