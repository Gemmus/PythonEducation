# Write an Elevator class that receives the numbers of the bottom and top floors as initializer parameters.
# The elevator has methods go_to_floor, floor_up and floor_down.
# A new elevator is always at the bottom floor.
# If you make elevator h for example the method call h.go_to_floor(5),
# the method calls either the floor_up or floor_down methods as many times as it needs to get to the fifth floor.
# The methods run the elevator one floor up or down and tell what floor the elevator is after each move.
# Test the class by creating an elevator in the main program,
# tell it to move to a floor of your choice and then back to the bottom floor.

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


elevator1 = Elevator(12)
elevator1.go_to_floor(7)
elevator1.go_to_floor(2)
elevator1.go_to_floor(15)
elevator1.go_to_floor(-4)
