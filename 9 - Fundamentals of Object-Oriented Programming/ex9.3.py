# Again, extend the program by adding a new drive method that receives the number of hours as a parameter.
# The method increases the travelled distance by how much the car has travelled in constant speed in the given time.
# Example: The travelled distance of car object is 2000 km. The current speed is 60 km/h.
# Method call car.drive(1.5) increases the travelled distance to 2090 km.

class Vehicle:
    def __init__(self, plate, maximum_speed, current_speed=0, distance=0):
        self.plate = plate
        self.maximum_speed = maximum_speed
        self.current_speed = current_speed
        self.distance = distance

    def number_of_hours(self, hour=0):
        self.distance = self.distance + hour * 60


car = Vehicle("ABC-123", 142, 60, 2000)
car.number_of_hours(+5)     # +300km
print(f"{car.distance:d}")
car.number_of_hours(+9)     # +540 km
print(f"{car.distance:d}")
car.number_of_hours(+200)     # +12000 km
print(f"{car.distance:d}")


print(f"""
The car with the registration plate {car.plate:s} has the maximum speed of {car.maximum_speed:d} km/h.
The current speed is {car.current_speed:d} km/h and has travelled {car.distance:d} km.""")
