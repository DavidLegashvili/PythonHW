#Лотерея скидок
res = 0
summa = []
while True:
    price = float(input("Введите стоимость товара(Вводить до 00):"))
    if price > 0:
        summa.append(price)
    elif price == 00:
        break
while True:
    if sum(summa) % 2 == 0:
        res = sum(summa) // 2
    if res % 2 != 0:
        break
print("К оплате:", res)

#Не работает чета
