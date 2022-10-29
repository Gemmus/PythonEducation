# Extend the previously written Car class by adding two subclasses: ElectricCar and GasolineCar.
# Electric cars have the capacity of the battery in kilowatt-hours as their property.
# Gasoline cars have the volume of the tank in liters as their property.
# Write initializers for the subclasses.
# For example, the initializer of electric cars receives the registration number,
# maximum speed and battery capacity as its parameter.
# It calls the initializer of the base class to set the first two properties and then sets its capacity.
# Write a main program where you create one electric car (ABC-15, 180 km/h, 52.5 kWh)
# and one gasoline car (ACD-123, 165 km/h, 32.3 l).
# Select speeds for both cars, make them drive for three hours and print out the values of their kilometer counters.

import random


class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = random.randint(80, maximum_speed)

    def accelerate(self):
        change_of_speed = random.randint(-20, 20)
        self.current_speed += change_of_speed
        if self.current_speed < 0:
            self.current_speed = 0
        elif self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        return self.current_speed

    def print_information(self):
        print("pass")


class ElectricCar(Car):
    def __init__(self, registration_number, maximum_speed, battery):
        super().__init__(registration_number, maximum_speed)
        self.battery = battery

    def print_information(self):
        print("pass")


class GasolineCar(Car):
    def __init__(self, registration_number, maximum_speed, tank_volume):
        super().__init__(registration_number, maximum_speed)
        self.tank_volume = tank_volume

    def print_information(self):
        print("pass")


ec1 = ElectricCar("ABC-15", 180, 52.5)   # 52.5 kWh
gc1 = GasolineCar("ACD-123", 165, 32.3)  # 32.3 l
# Select speeds for both cars, make them drive for three hours and print out the values of their kilometer counters.
hours = 1
travelled_distance1 = travelled_distance2 = 0
while hours < 4:
    travelled_distance1 += ec1.accelerate()
    travelled_distance2 += gc1.accelerate()
    print(f"The electric car travelled {travelled_distance1}km during the period of {hours} hour(s).")
    print(f"The gasoline car travelled {travelled_distance2}km during the period of {hours} hour(s).")
    hours += 1

print(f"The electric car has travelled a total of {travelled_distance1}km.")
print(f"The gasoline car has travelled a total of {travelled_distance2}km.")
