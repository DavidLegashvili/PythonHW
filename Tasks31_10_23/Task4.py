amount = int(input("Введите кол-во товаров:"))
first = 10.95
secondetc = 2.95

def sale(amount):
    if amount > 2:
        res = round(10.95 + 2.95 * amount - 1, 2)
    elif amount == 2:
        res = round(10.95 + 2.95, 2)
    elif amount == 1:
        res = 10.95
    else:
        print("Вы ничего не заказали, емае")
    return res
sale(amount)
resultat = sale(amount)

print(resultat)