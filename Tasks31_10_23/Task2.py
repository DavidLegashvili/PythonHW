#2.	Создайте словарь гороскопов, где по ключу “знак зодиака” хранится список предсказаний. 
#Запросите у пользователя ввод знака зодиака и выведите случайное предсказание для этого знака из списка.

zodiac_sign = {
    "овен": "Сейчас бы верить знакам зодиака:/",
    "телец": "Будешь работать - будет результат",
    "близнецы": "Можешь ничего не делать, ты и так хорош",
    "рак": "Ну сегодня не твой день, чего поделать",
    "лев": "Ты ЛЕВ!1!11!1"
}

sign = input("Введите знак зодиака\n").lower()

if zodiac_sign.get(sign) != None:
    print(zodiac_sign.get(sign))

else:
    print("Ничего про тебя не знаю")


