mass = float(input("Введите массу тела:"))
height = float(input("Введите рост:"))
res = (mass / height ** 2) * 10000
print(round(res, 2))