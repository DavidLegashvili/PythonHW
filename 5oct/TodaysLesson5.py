#DictNames

names = {
    "Dmitry": 32,
    "Anatoly": 18
}

names["Alex"] = 26

sum = names.setdefault("Dmitry") + names.setdefault("Anatoly") + names.setdefault("Alex")
print(sum)