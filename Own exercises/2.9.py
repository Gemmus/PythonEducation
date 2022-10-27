class Cat:
    number_of_cats = 0

    def __init__(self, name, birth_year, sound="Meow"):
        self.name = name
        self.birth_year = birth_year
        self.sound = sound
        Cat.number_of_cats += 1

    def meow(self, times):
        for i in range(times):
            print(self.sound)
        return


cat1 = Cat("Tapio", 2012, "Prr prr")
cat2 = Cat("Mirri", 2020)
print(f"{cat1.name} was born in {cat1.birth_year}.")
cat1.meow(2)
print(f"{cat2.name} was born in {cat2.birth_year}.")
cat2.meow(3)

print(f"The number of cats in the list so far is: {Cat.number_of_cats}.")
