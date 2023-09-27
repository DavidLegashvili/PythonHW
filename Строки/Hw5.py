email = input("Введите свою почту")
res = email.find("@")
print(email[:res])