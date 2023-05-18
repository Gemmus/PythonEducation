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
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = random.randint(0, self.max_speed)
        self.travelled_distance = 0

    def accelerate(self, change_of_speed):
        self.current_speed += change_of_speed
        if self.current_speed < 0:
            self.current_speed = 0
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours
        return self.travelled_distance


class ElectricCar(Car):
    def __init__(self, registration_number, max_speed, battery_capacity):
        super().__init__(registration_number, max_speed)
        self.battery_capacity = battery_capacity


class GasolineCar(Car):
    def __init__(self, registration_number, max_speed, tank_volume):
        super().__init__(registration_number, max_speed)
        self.tank_volume = tank_volume


electric_car1 = ElectricCar("ABC-15", 180, 52.5)  # km/h, kWh
gasoline_car1 = GasolineCar("ACD-123", 165, 32.3)  # km/h, l

for i in range(3):
    change_speed = random.randint(-50, 50)
    electric_car1.accelerate(change_speed)
    electric_car1.drive(1)
    change_speed = random.randint(-50, 50)
    gasoline_car1.accelerate(change_speed)
    gasoline_car1.drive(1)

print(f'The electric car travelled {electric_car1.travelled_distance} km in 3 hours.')
print(f'The gasoline car travelled {gasoline_car1.travelled_distance} km in 3 hours.')
