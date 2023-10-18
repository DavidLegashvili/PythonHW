help_input = "".lower()

def avtootvet(help_input):
    fst = help_input.find("расп")
    if fst != -1:
        print("Расписание:\n1.....\n2......\n3.....\n4.....")
    scd = help_input.find("трен")
    if scd != -1:
        print("Данные тренера:\nНомер телефона -\nПочта - ")
    thrd = help_input.find("олпат")
    if thrd != -1:
        print("Сумма к оплате: ....")
    frth = help_input.find("адрес")
    if frth != -1:
        print("Наш адрес:....")
    ffth = help_input.find("отзы")
    if ffth != -1:
        print("Отзывы клиентов можно посмотреть во вкладке 'отзывы'")
    
    