help_input = "".lower()
def avtootvet(help_input):
    fst = help_input.find("расп")
    if fst != -1:
        print("Расписание:\n1.....\n2......\n3.....\n4.....")
    scd = help_input.find("трен")
    if scd != -1:
        trener = input("1. Перечень тренеров\n2. Данные конкретного тренера\n").lower()
        if trener == trener.find("переч") or trener == "1":
            print("Наши тренеры:\nДавид Легашвили\nОлеся Савельева\nСавва Ларханиди")
        elif trener == trener.find("данные") or trener == "2":
            concr_tren = input("Введите ФИО тренера:\n")
            print("Данные тренера", concr_tren, ":\nНомер телефона -\nПочта - ")
    thrd = help_input.find("оплат")
    if thrd != -1:
        summa = input("1.Сумма к оплате\n2.Возврат средств\n3.Сумма за определенные услуги\n").lower()
        if summa == summa.find("оплат") or summa == "1":
            print("Сумма к оплате: ....\nОплатить можно переводом на счет:.....")
        elif summa == summa.find("возвр") or summa == "2":
            print("Возврат средств можно оформить по телефону +7....\nПожалуйста, сообщите нам, если Вам что-то не понравилось")
        elif summa == summa.find("опред") or summa == "3":
            print("Для уточнения суммы позвоните по номеру +7.......")
    frth = help_input.find("адрес")
    if frth != -1:
        address = input("1. Адрес головного офиса\n2. Адреса залов\n").lower()
        if address == address.find("гол") or address == "1":        
            print("Адрес нашего офиса:....")
        elif address == address.find("зал") or address == "2":
            print("Адреса всех наших залов:\nг. Сочи, ул.Армавирская 120\nг. Челябинск, ул.Энтузиастов 12\nг. Казань, ул.Ленина 24")
    ffth = help_input.find("отзы")
    if ffth != -1:
        print("Отзывы клиентов можно посмотреть во вкладке 'отзывы'")


    
