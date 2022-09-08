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

    def change_of_speed(self, change):
        self.current_speed += change
        if self.current_speed < 0:
            self.current_speed = 0
        elif self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed

    def number_of_hours(self, hour):
        self.distance += hour




car = Vehicle("ABC-123", 142)
car.change_of_speed(+30)
print(f"{car.current_speed:d}")
car.change_of_speed(+70)
print(f"{car.current_speed:d}")
car.change_of_speed(+50)

print(f"""
The car with the registration plate {car.plate:s} has the maximum speed of {car.maximum_speed:d} km/h.
Its current speed is {car.current_speed:d} km/h.""")

car.change_of_speed(-200)

print(f"""
The car with the registration plate {car.plate:s} has the maximum speed of {car.maximum_speed:d} km/h.
Its current speed is {car.current_speed:d} km/h.""")
