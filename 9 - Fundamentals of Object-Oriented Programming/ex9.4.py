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
# Each car is made to drive for one hour. This
# The race continues until one of the cars has advanced at least 10,000 kilometers.
# Finally, the properties of each car are printed out formatted into a clear table.

import random


class Race:
    def __init__(self, plate, current_speed, distance=0):
        self.plate = plate
        self.current_speed = current_speed
        self.distance = distance

    def Acceleration(self, change):
        self.current_speed += change
        change(int(random.uniform(-10, +15)))
        if self.current_speed < 100:
            self.current_speed = 100
        elif self.current_speed > 200:
            self.current_speed = 200
        return


# main program:

list1 = []
a = 1
for i in range(10):
    b = int(random.uniform(100, 200))
#    print(a)
#    print(b)
    car = (a, b)
    print(car)
    a += 1


#print (f"{Race.created} have been created so far.")

# for n in range(len(list1)):
#     print(list1[n])
