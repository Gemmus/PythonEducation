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


class Car:
    def __init__(self, registration_number, max_speed, current_speed=0, travelled_distance=0):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = current_speed
        self.travelled_distance = travelled_distance

    def accelerate(self, change_of_speed):
        self.current_speed += change_of_speed
        if self.current_speed < 0:
            self.current_speed = 0
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours
        return self.travelled_distance


car_list = []
for i in range(10):
    registration_plate = 1 + i
    maximum_speed = random.randint(100, 200)
    current_speed = random.randint(0, maximum_speed)
    car_list.append(Car(registration_plate, maximum_speed, current_speed))

hour = 0
race = True
while race:
    hour += 1
    for i in range(len(car_list)):
        speed_change = random.randint(-10, 15)
        car_list[i].accelerate(speed_change)
        travelled_distance = car_list[i].drive(1)
        if travelled_distance > 10000:
            print(f'At the {hour}th hour of the race:')
            for ii in range(len(car_list)):
                print(f'ABC-{car_list[ii].registration_number}: {car_list[ii].travelled_distance} km')
            race = False



