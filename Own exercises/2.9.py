class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age


d1 = Dog("Toto", 4)
print(d1.get_name(), d1.get_age())
d2 = Dog("Minttu", 9)
print(d2.get_name(), d2.get_age())
d2.set_age(10)
print(d2.get_name(), d2.get_age())