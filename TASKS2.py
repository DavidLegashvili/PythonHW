#Успеваемость
input_res = 0
res = []
while input_res > 0:
    input_res = input("Введите оценку:")
    res.append(input_res)
    if res == 0:
        break
res1 = len(res)
usp = sum(res) / sum(res1)
print("res1\nusp")
