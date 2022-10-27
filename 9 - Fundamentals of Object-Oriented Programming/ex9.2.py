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

class Car:
    def __init__(self, registration_number, maximum_speed, current_speed=0, travelled_distance=0):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = current_speed
        self.travelled_distance = travelled_distance

    def accelerate(self, change_of_speed):
        self.current_speed += change_of_speed
        if self.current_speed < 0:
            self.current_speed = 0
        elif self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        return


car1 = Car("ABC-123", 142)
car1.accelerate(+30)
# print(f"{car1.current_speed} km/h")
car1.accelerate(+70)
# print(f"{car1.current_speed} km/h")
car1.accelerate(+50)
print(f"""
The car with the registration plate {car1.registration_number:s} has the maximum speed of {car1.maximum_speed:d} km/h.
The current speed is {car1.current_speed:d} km/h and has travelled {car1.travelled_distance:d} km.""")

car1.accelerate(-200)
print(f"""
The car with the registration plate {car1.registration_number:s} has the maximum speed of {car1.maximum_speed:d} km/h.
The current speed is {car1.current_speed:d} km/h and has travelled {car1.travelled_distance:d} km.""")
