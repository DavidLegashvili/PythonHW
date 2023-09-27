budjet = int(input("Введите бюджет:"))
price = float(input("Введите стоимость товара:"))
amount = int(budjet // price)
print("Вы можете купить", amount, "единиц этого товара")