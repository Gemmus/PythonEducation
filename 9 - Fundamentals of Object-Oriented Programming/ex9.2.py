# Extend the program by adding an accelerate method into the new class.
# The method should receive the change of speed (km/h) as a parameter.
# If the change is negative, the car reduces speed.
# The method must change the value of the speed property of the object.
# The speed of the car must stay below the set maximum and cannot be less than zero.
# Extend the main program so that the speed of the car is first increased by +30 km/h,
# then +70 km/h and finally +50 km/h.
# Then print out the current speed of the car.
# Finally, use the emergency brake by forcing a -200 km/h change on the speed and then print out the final speed.
# The travelled distance does not have to be updated yet.

class Vehicle:
    def __init__(self, plate, maximum_speed, current_speed=0, distance=0):
        self.plate = plate
        self.maximum_speed = maximum_speed
        self.current_speed = current_speed
        self.distance = distance

    def change_of_speed(self, change):
        self.current_speed += change
        if self.current_speed < 0:
            self.current_speed = 0
        elif self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        return


car = Vehicle("ABC-123", 142)
car.change_of_speed(+30)
print(f"{car.current_speed:d}")
car.change_of_speed(+70)
print(f"{car.current_speed:d}")
car.change_of_speed(+50)

print(f"""
The car with the registration plate {car.plate:s} has the maximum speed of {car.maximum_speed:d} km/h.
The current speed is {car.current_speed:d} km/h.""")

car.change_of_speed(-200)

print(f"""
The car with the registration plate {car.plate:s} has the maximum speed of {car.maximum_speed:d} km/h.
The current speed is {car.current_speed:d} km/h.""")
