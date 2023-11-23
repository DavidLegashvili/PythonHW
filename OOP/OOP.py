#1.	Создай класс Animal. 

class Animal:
    def __init__(self, animal, voice):
        self.animal = animal
        self.voice = voice

    def make_voice(self):
        print(self.voice)


dog = Animal("dog", "Гав")
cat = Animal("cat", "Мяу")

dog.make_voice()
cat.make_voice()




        
        

        