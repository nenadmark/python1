class Animal:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    
    def say_hello(self):
        print("Hello")


class Cat(Animal):
    pass


class Dog(Animal):
    def say_hello(self):
        print("Woof!")
        super().say_hello()


class Bird:
    name = "Birdy"
    color = "Yellow"


cat_1 = Cat("Catty", "black")
cat_1.say_hello()
print(cat_1.name)

dog_1 = Dog("Bla", "white")
dog_1.say_hello()

bird_1 = Bird()
print(bird_1.name)

bird_2 = Bird()
print(bird_2.name)