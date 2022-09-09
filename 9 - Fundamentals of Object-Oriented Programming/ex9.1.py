# Write a Car class that has the following properties:
# registration number, maximum speed, current speed and travelled distance.
# Add a class initializer that sets the first two of the properties based on parameter values.
# The current speed and travelled distance of a new car must be automatically set to zero.
# Write a main program where you create a new car (registration number ABC-123, maximum speed 142 km/h).
# Finally, print out all the properties of the new car.

class Vehicle:
    def __init__(self, plate, maximum_speed, current_speed=0, distance=0):
        self.plate = plate
        self.maximum_speed = maximum_speed
        self.current_speed = current_speed
        self.distance = distance


car = Vehicle("ABC-123", 142)


print(f"""
The car with the registration plate {car.plate:s} has the maximum speed of {car.maximum_speed:d} km/h.
The current speed is {car.current_speed:d} km/h and has travelled {car.distance:d} km.""")
