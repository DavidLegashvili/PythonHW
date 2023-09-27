#Настольная игра
input_game = ""
games = []
while True:
    if input_game in games:
        print("Такая игра уже есть")
    else:
        games.append(input_game)
        print("Игра добавлена")