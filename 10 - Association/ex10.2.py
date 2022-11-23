# Extend the previous program by creating a Building class.
# The initializer parameters for the classes are the numbers of the bottom
# and top floors and the number of elevators in the building.
# When a building is created, the building creates the required number of elevators.
# The list of elevators is stored as a property of the building.
# Write a method (run_elevator) that accepts the number of the elevator and the destination floor as its parameters.
# In the main program, write the statements for creating a new building and running the elevators of the building.

class Elevator:
    def __init__(self, bottom_floor=1, top_floor=50):
        self.bottom = bottom_floor
        self.top = top_floor
        self.current = bottom_floor

    def go_to_floor(self, floor):
        if self.top > floor > self.current:
            for i in range(floor-self.current):
                self.floor_up()
        elif self.bottom < floor < self.current:
            for i in range(self.current - floor):
                self.floor_down()
        print(f"You are at floor {self.current}.")
        return self.current

    def floor_up(self):
        if self.current < self.top:
            self.current += 1
        print(f"Moving up. Floor {self.current}")

    def floor_down(self):
        if self.current > self.bottom:
            self.current -= 1
        print(f"Moving down. Floor {self.current}")


class Building:
    def __init__(self, bottom_floor, top_floor, number_of_elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.number_of_elevators = number_of_elevators
        self.list_of_elevators = []
        for i in range(number_of_elevators):
            elevator = Elevator(bottom_floor, top_floor)
            self.list_of_elevators.append(elevator)

    def run_elevator(self, number, destination):
        called_elevator = self.list_of_elevators[number-1]
        return called_elevator.go_to_floor(destination)


building1 = Building(1, 15, 4)
new_floor1 = building1.run_elevator(1, 8)
print(f"Elevator 1 is at floor {new_floor1}.")

new_floor1 = building1.run_elevator(1, 5)
print(f"Elevator 1 is at floor {new_floor1}.")

new_floor2 = building1.run_elevator(2, 3)
print(f"Elevator 2 is at floor {new_floor2}.")

new_floor2 = building1.run_elevator(2, 6)
print(f"Elevator 2 is at floor {new_floor2}.")

new_floor3 = building1.run_elevator(3, 10)
print(f"Elevator 3 is at floor {new_floor3}.")

new_floor3 = building1.run_elevator(3, 4)
print(f"Elevator 3 is at floor {new_floor3}.")
