#Повторяющиеся элементы

list = []
while True:
    input_list = int(input("Введите числа(вводить до 0)"))
    if input_list > 0:
        list.append(input_list)
    elif input_list == 0:
        break

h = 0
for i in list:
    if list.count(i) > 1:
        h += 1
        break

if h > 0:
    print("Числа повторяются")
else:
    print("Числа уникальны")


        
        
        
