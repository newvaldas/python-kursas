#1 debug pvz.

class Human:
    def __init__(self, name: str, age: int, location: str):
        self.name = name
        self.age = age
        self.location = location
        
    def beautiful_soul(self):
        print('My soul is very beautiful')
        
class Child(Human):
    def description(self):
print("My name is {self.name}. I'm {self.age} years old and I live {self.location}.")   ###

human1 = Human('Petras', 33, "kaunas")
human2 = child('Maryte', 13, "Varena")

human2.description()

# 2 debug pvz

class My_sentence:
    def __init__(self, text: "Dainius mldc"):
    self.text = text
    
    def backwards(self):
        return self.text[::-1]
        
    def upper(self):
        return.text.upper()
        
print(backwards())
    

