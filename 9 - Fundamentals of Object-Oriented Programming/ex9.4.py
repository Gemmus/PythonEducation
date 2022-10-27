# Now we will program a car race. The travelled distance of a new car is initialized as zero.
# At the beginning of the main program, create a list that consists of 10 car objects created using a loop.
# The maximum speed of each new car is a random value between 100 km/h and 200 km/h.
# The registration numbers are created as follows: "ABC-1", "ABC-2" and so on.
#
# Now the race begins.
# One per every hour of the race, the following operations are performed:
#
# The speed of each car is changed so that the change in speed is a random value between -10 km/h and +15 km/h.
# This is done using the accelerate method.
#
# Each car is made to drive for one hour. This is done with the drive method.
# The race continues until one of the cars has advanced at least 10,000 kilometers.
# Finally, the properties of each car are printed out formatted into a clear table.

import random


class Race:
    def __init__(self, registration_number, current_speed, travelled_distance=0):
        self.registration_number = registration_number
        self.current_speed = current_speed
        self.travelled_distance = travelled_distance

    def accelerate(self, change_of_speed):
        self.current_speed += change_of_speed
        if self.current_speed < 100:
            self.current_speed = 100
        elif self.current_speed > 200:
            self.current_speed = 200
        return self.current_speed

    def drive(self, addition):
        self.travelled_distance += addition
        return self.travelled_distance


car_list = []
plate_number = 1
for i in range(10):
    speed = random.randint(100, 200)
    new_car = Race(plate_number, speed)
    car_list.append(new_car)
    plate_number += 1

race_over = False
circle = 1
while not race_over:
    print("\nRound " + str(circle) + ":")
    for car in car_list:
        acceleration = random.randint(-10, +15)
        speed = car.accelerate(acceleration)
        distance = car.drive(speed)
        print("[ABC-" + str(car.registration_number) + "] speed: " + str(speed) + " km/h  distance: " + str(distance) + " km")
        if distance >= 10000:
            race_over = True
    circle += 1
