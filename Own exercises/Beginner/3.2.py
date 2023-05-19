class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")

    def speak(self):
        print("I don't know what to say.")


class Cat(Pet):
    def speak(self):
        print("Meow")


class Dog(Pet):
    def speak(self):
        print("Bark")


class Fish(Pet):
    pass


p = Pet("Bubbles", 7)
p.show()
p.speak()
c = Cat("Tapio", 10)
c.show()
c.speak()
d = Dog("Minttu", 6)
d.show()
d.speak()
f = Fish("Goldie", 0.5)
f.show()
f.speak()
