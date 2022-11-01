# Extend the program again by adding a method fire_alarm that does not receive any parameters
# and moves all elevators to the bottom floor.
# Continue the main program by causing a fire alarm in your building.

class Elevator:
    def __init__(self, bottom=1, top=50):
        self.bottom_floor = bottom
        self.top_floor = top
        self.current_floor = bottom

    def go_to_floor(self, floor):
        if self.bottom_floor <= floor <= self.top_floor:
            if floor > self.current_floor:
                numbers_of_floor = floor - self.current_floor
                for i in range(numbers_of_floor):
                    self.floor_up()
            if floor < self.current_floor:
                numbers_of_floor = self.current_floor - floor
                for i in range(numbers_of_floor):
                    self.floor_down()
        return self.current_floor

    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
        print(f"Moving up. Floor {self.current_floor}")
        return self.current_floor

    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
        print(f"Moving down. Floor {self.current_floor}")
        return self.current_floor


class Building:
    def __init__(self, elevators=0, bottom=1, top=50):
        self.num_of_elevators = elevators
        self.bottom_floor = bottom
        self.top_floor = top
        self.list_of_elevators = []
        for i in range(elevators):
            elevator = Elevator(bottom, top)
            self.list_of_elevators.append(elevator)

    def run_elevator(self, number_of_elevator, destination_floor):
        called_elevator = self.list_of_elevators[number_of_elevator-1]
        return called_elevator.go_to_floor(destination_floor)

    def fire_alarm(self):
        for i in range(self.num_of_elevators):
            self.list_of_elevators[i].go_to_floor(1)


building1 = Building(4, 1, 15)
new_floor = building1.run_elevator(1, 8)
print(f"Elevator 1 is at floor {new_floor}.")

new_floor = building1.run_elevator(2, 3)
print(f"Elevator 2 is at floor {new_floor}.")

new_floor = building1.run_elevator(3, 10)
print(f"Elevator 3 is at floor {new_floor}.")

new_floor = building1.run_elevator(4, 5)
print(f"Elevator 4 is at floor {new_floor}.")

building1.fire_alarm()
