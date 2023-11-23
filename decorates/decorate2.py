#1 задание не прогрузилось, там какие-то проблемы с кодировщиком.

"""
Напишите программу добавляющую в рецепт бутерброда ингридиенты "Салат" и "Ананасы" с помощью декораторов.
"""

def decorate(func):
    def wrapper():
        print("Рецепт салата:\n1.Томаты\n2.Огурцы\n3.Лук")
        func()
    return wrapper
    

def functionrecept():
    print("А также Салат и Ананасы")

decorator = decorate(functionrecept)
decorator()