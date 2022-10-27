from random import randint


class Car:

    def __init__(self, registration_number, max_speed, current_speed=0, distance_travelled=0):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = current_speed
        self.distance_travelled = distance_travelled

    def accelerate(self, change_of_speed):
        self.current_speed = self.current_speed + change_of_speed
        if self.current_speed < 0:
            self.current_speed = 0
        elif self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        return

    def drive(self, hours):
        self.distance_travelled = self.distance_travelled + (hours * self.current_speed)
        return


cars = []

for x in range(1, 11):
    registration_number = "ABC-" + str(x)
    max_speed = randint(100, 200)
    cars.append(Car(registration_number, max_speed))

for car in cars:
    while car.distance_travelled <= 10000:
        car.accelerate(randint(-10, 15))
        car.drive(1)

for car in cars:
    print(f"Registration number: {car.registration_number}, Maximum speed: {car.max_speed}, Current speed: {car.current_speed}, Distance travelled: {car.distance_travelled}.")
