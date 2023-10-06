#1 Проврка на палиндром.

word = input("Введите слово:")
if word[::-1] == word:
    print("Палиндром")
else:
    print("Нет")