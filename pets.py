class Pet:
    def __init__(self, name, age, sound, food):
        self.name = name
        self.age = age
        self.sound = sound
        self.food = food

    def show(self):
        print(f"I'm {self.name}, I'm {self.age} years old and I say {self.sound}")

    def speak(self):
        print(f"I say {self.sound}")

class Cat(Pet):
    def __init__(self, name, age):
        super().__init__(name, age, "meow", "mise")  # Properly initialize parent class

class Dog(Pet):
    def __init__(self, name, age):
        super().__init__(name, age, "woof", "cat")

class Fish(Pet):
    def __init__(self, name, age):
        super().__init__(name, age, "bubble", "smaller beings")


my_cat = Cat("mila", 17)
my_dog = Dog("yousef",12)
my_fish = Fish("omar",14)

my_cat.show()  
my_dog.show()
my_fish.show() 