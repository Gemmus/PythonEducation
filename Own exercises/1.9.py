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
        return self.current_speed

    def get_current_speed(self):
        return self.current_speed


car = Vehicle("ABC-123", 142)
car.change_of_speed(+30)
print(f"{car.get_current_speed():d}")
car.change_of_speed(+70)
print(f"{car.get_current_speed():d}")
car.change_of_speed(+50)

print(f"""
The car with the registration plate {car.plate:s} has the maximum speed of {car.maximum_speed:d} km/h.
Its current speed is {car.get_current_speed():d} km/h.""")

car.change_of_speed(-200)

print(f"""
The car with the registration plate {car.plate:s} has the maximum speed of {car.maximum_speed:d} km/h.
Its current speed is {car.get_current_speed():d} km/h.""")
