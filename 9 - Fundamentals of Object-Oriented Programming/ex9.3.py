# Again, extend the program by adding a new drive method that receives the number of hours as a parameter.
# The method increases the travelled distance by how much the car has travelled in constant speed in the given time.
# Example: The travelled distance of car object is 2000 km. The current speed is 60 km/h.
# Method call car.drive(1.5) increases the travelled distance to 2090 km.

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

    def drive(self, number_of_hours):
        for i in range(number_of_hours):
            self.travelled_distance += self.current_speed
        return


car1 = Car("ABC-123", 142)
car1.accelerate(+90)
# print(f"{car1.current_speed} km/h * 5 hours")
car1.drive(5)
print(f"""
The car with the registration plate {car1.registration_number:s} has the maximum speed of {car1.maximum_speed:d} km/h.
The current speed is {car1.current_speed:d} km/h and has travelled {car1.travelled_distance:d} km.""")

car1.accelerate(-20)
# print(f"\n{car1.current_speed} km/h * 10 hours")
car1.drive(10)
print(f"""
The car with the registration plate {car1.registration_number:s} has the maximum speed of {car1.maximum_speed:d} km/h.
The current speed is {car1.current_speed:d} km/h and has travelled {car1.travelled_distance:d} km.""")

car1.accelerate(+30)
# print(f"\n{car1.current_speed} km/h * 200 hours")
car1.drive(200)
print(f"""
The car with the registration plate {car1.registration_number:s} has the maximum speed of {car1.maximum_speed:d} km/h.
The current speed is {car1.current_speed:d} km/h and has travelled {car1.travelled_distance:d} km.""")
