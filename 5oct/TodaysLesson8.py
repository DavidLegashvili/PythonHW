num_list = []
sec_num = int(input("Введите число:"))
while True:
    num = int(input("Введите числа(до 0:)"))
    if num > 0:
        num_list.append(num)
    else:
        break

for i in num_list:
    for j in num_list:
        if i + j == sec_num:
            a = i
            b = j
            break

print(a, b)


