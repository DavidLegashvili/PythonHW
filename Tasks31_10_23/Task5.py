#1 черпак = 16 чайных ложек 
#столовая ложка = 4 чайным ложкам 
#и чайная ложка. 

chn = 1
stol = chn * 4
chrpk = chn * 16

lojka = int(input("Кол-во чайных ложек: "))

def lojkaemae(lojka):
    print(f"Вы ввели {lojka} чайных ложек\nЭто {lojka/4} столовых ложек\nИли {lojka/16} черпаков")

lojkaemae(lojka)