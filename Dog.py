
class Dog:
    quantity = 0
    def __init__(self,name,age):
        self.name = name
        self.age = age
        Dog.quantity += 1
        

bulldog = Dog("Sammy",3) 
hosky = Dog("Alex",5)
hosky.quantity = 1
print(Dog.quantity)
print(hosky.quantity)


class TextHandler:
    def __init__(self):
        self.text = ""

    def get_input(self):
        self.text = input("Enter something: ")

    def print_upper(self):
        print(self.text.upper())




class Dog:
    def walk(self):
        return "*walking*"
    def speak(self):
        return "Woof!"
class JackRussellTerrier(Dog):
    def talk(self):
        return super().speak()
bobo = JackRussellTerrier()
print(bobo.talk())