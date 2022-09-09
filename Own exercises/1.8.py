class Dog:
    def __init__(self, name, birth_year, sound="Woof woof"):
        self.name = name
        self.birth_year = birth_year
        self.sound = sound

    def bark(self, times):
        for i in range(times):
            print(self.name + " barks: " + self.sound)
        return


class Hotel:
    def __init__(self):
        self.dogs = []

    def dog_check_in(self, dog):
        self.dogs.append(dog)
        print(dog.name + " checked in")
        return

    def dog_check_out(self, dog):
        self.dogs.remove(dog)
        print(dog.name + " checked out")
        return

    def greet_dogs(self):
        for dog in self.dogs:
            dog.bark(1)


# Main program
dog1 = Dog("Rascal", 2018)
dog2 = Dog("Boi", 2022, "Yip yip yip")

hotel = Hotel()

hotel.dog_check_in(dog1)
hotel.dog_check_in(dog2)
hotel.greet_dogs()

hotel.dog_check_out(dog1)
hotel.greet_dogs()
