my_variable = "This is my global variable"

# print("my_model has been successfully imported")


def write_backwards(sentence: str) -> str:
      return sentence[::-1]


class Person():
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f"Hi my name is {self.name}, I am {self.age}")

        