# Extend the previous program by creating a Building class.
# The initializer parameters for the classes are the numbers of the bottom
# and top floors and the number of elevators in the building.
# When a building is created, the building creates the required number of elevators.
# The list of elevators is stored as a property of the building.
# Write a method (run_elevator) that accepts the number of the elevator and the destination floor as its parameters.
# In the main program, write the statements for creating a new building and running the elevators of the building.

class Elevator:
    def __init__(self, top_floor, bottom_floor=0):
        self.top_floor = top_floor
        self.bottom_floor = bottom_floor
        self.current_floor = bottom_floor

    def floor_up(self):
        if self.bottom_floor <= (self.current_floor + 1) <= self.top_floor:
            self.current_floor += 1
            print(f'Floor up, new floor: {self.current_floor}')
        else:
            self.current_floor = self.current_floor
            print(f'Floor: {self.current_floor}, at top floor')

    def floor_down(self):
        if self.top_floor >= (self.current_floor - 1) >= self.bottom_floor:
            self.current_floor -= 1
            print(f'Floor down, new floor: {self.current_floor}')
        else:
            self.current_floor = self.current_floor
            print(f'Floor: {self.current_floor}, at bottom floor')

    def go_to_floor(self, target_floor):
        if target_floor > self.current_floor:
            for i in range(target_floor - self.current_floor):
                self.floor_up()
        if target_floor < self.current_floor:
            for i in range(self.current_floor - target_floor):
                self.floor_down()
        return self.current_floor


class Building:
    def __init__(self, top_floor, bottom_floor=0, total_elevator=0):
        self.top_floor = top_floor
        self.bottom_floor = bottom_floor
        self.total_elevator = total_elevator
        self.elevators = []
        for i in range(self.total_elevator):
            self.elevators.append(Elevator(self.top_floor, self.bottom_floor))

    def run_elevator(self, which_elevator, target_floor):
        return self.elevators[which_elevator-1].go_to_floor(target_floor)


building1 = Building(20, 0, 5)
new_floor4 = building1.run_elevator(4, 7)
print(f'Elevator 4 is at floor {new_floor4}.')

new_floor2 = building1.run_elevator(2, 9)
print(f'Elevator 2 is at floor {new_floor2}.')

new_floor1 = building1.run_elevator(1, 4)
print(f'Elevator 1 is at floor {new_floor1}.')

new_floor4 = building1.run_elevator(4, 10)
print(f'Elevator 4 is at floor {new_floor4}.')

new_floor2 = building1.run_elevator(2, 3)
print(f'Elevator 2 is at floor {new_floor2}.')
