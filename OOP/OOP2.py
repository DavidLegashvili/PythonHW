# 3.Запрограммируй класс Rectangle 

class Rectangle:
    def __init__(self, len, wigh):
        self.len = len
        self.wigh = wigh

    def inp(self):
        leng = int(input("Длина: "))
        wight = int(input("Ширина: "))
        self.len = leng
        self.wigh = wight

    def info(self):
        print(f"Создан прямоугольник длиной {self.len}, шириной {self.wigh}")

    def P(self):
        print(f"Периметр равен {self.len * 2 + self.wigh * 2}")

rect = Rectangle("-", "-")
rect.inp()
rect.info()
rect.P()

#Done