# Extend the previous program by creating a Building class.
# The initializer parameters for the classes are the numbers of the bottom
# and top floors and the number of elevators in the building.
# When a building is created, the building creates the required number of elevators.
# The list of elevators is stored as a property of the building.
# Write a method (run_elevator) that accepts the number of the elevator and the destination floor as its parameters.
# In the main program, write the statements for creating a new building and running the elevators of the building.

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


building1 = Building(3)
new_floor = building1.run_elevator(1, 8)
print(f"Elevator 1 is at floor {new_floor}.")

new_floor = building1.run_elevator(1, 5)
print(f"Elevator 1 is at floor {new_floor}.")

new_floor = building1.run_elevator(2, 3)
print(f"Elevator 2 is at floor {new_floor}.")

new_floor = building1.run_elevator(2, 6)
print(f"Elevator 2 is at floor {new_floor}.")

new_floor = building1.run_elevator(3, 10)
print(f"Elevator 3 is at floor {new_floor}.")

new_floor = building1.run_elevator(3, 4)
print(f"Elevator 3 is at floor {new_floor}.")
