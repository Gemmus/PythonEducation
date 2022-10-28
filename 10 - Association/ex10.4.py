# This exercise continues the previous car race exercise from the last exercise set.
# Write a Race class that has the following properties:
# The class has an initializer that receives the name, kilometers and car list as parameters
# and sets their values to the corresponding properties in the class. The class has the following methods:
#
# - hour_passes, which performs the operations done once per hour in the original exercise:
#           generates a random change of speed for each car and calls their drive method.
# - print_status, which prints out the current information of each car as a clear, formatted table.
# - race_finished, which returns True if any of the cars has reached the finish line,
#           meaning that they have driven the entire distance of the race.
#
# Write a main program that creates an 8000-kilometer race called Grand Demolition Derby.
# The new race is given a list of ten cars similarly to the earlier exercise.
# The main program simulates the progressing of the race by calling the hour_passes in a loop,
# after which it uses the race_finished method to check if the race has finished.
# The current status is printed out using the print_status method every ten hours
# and then once more at the end of the race.
import random


class Car:
    def __init__(self, registration_number, current_speed, travelled_distance=0):
        self.registration_number = registration_number
        self.current_speed = current_speed
        self.travelled_distance = travelled_distance

    def drive(self, change_of_speed):
        self.current_speed += change_of_speed
        if self.current_speed < 100:
            self.current_speed = 100
        elif self.current_speed > 200:
            self.current_speed = 200
        self.travelled_distance += self.current_speed
        return self.current_speed, self.travelled_distance

    def get_plate(self):
        return self.registration_number

    def get_current_speed(self):
        return self.current_speed

    def get_travelled_distance(self):
        return self.travelled_distance


class Race:
    def __init__(self, name, kilometers, car_list):
        self.name = name
        self.kilometers = kilometers
        self.car_list = car_list

    def hour_passes(self):
        for vehicle in self.car_list:
            change_of_speed = random.randint(-10, +15)
            vehicle.drive(change_of_speed)

    def print_status(self):
        for vehicle in self.car_list:
            print(
                f"[ABC-{vehicle.get_plate()} speed:{vehicle.get_current_speed()} km/h distance:{vehicle.get_travelled_distance()} km")

    def race_finished(self):
        race_over = False
        for car in self.car_list:
            travelled_distance = car.get_travelled_distance()
            if travelled_distance >= self.kilometers:
                race_over = True
        return race_over


list_of_car = []
plate_number = 1
for i in range(10):
    speed = random.randint(100, 200)
    new_car = Car(plate_number, speed)
    list_of_car.append(new_car)
    plate_number += 1

race1 = Race("Grand Demolition Derby", 8000, list_of_car)
print(f"Welcome to the infamous {race1.kilometers} km long {race1.name}!")

progress = False
hour = 1
while not progress:
    race1.hour_passes()
    progress = race1.race_finished()
    if hour % 10 == 0:
        print(f"\n{hour} hours into the race:")
        race1.print_status()
    hour += 1

print(f"\n{race1.name} has ended! The result is:\n")
race1.print_status()
