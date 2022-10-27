# Write an Elevator class that receives the numbers of the bottom and top floors as initializer parameters.
# The elevator has methods go_to_floor, floor_up and floor_down.
# A new elevator is always at the bottom floor.
# If you make elevator h for example the method call h.go_to_floor(5),
# the method calls either the floor_up or floor_down methods as many times as it needs to get to the fifth floor.
# The methods run the elevator one floor up or down and tell what floor the elevator is after each move.
# Test the class by creating an elevator in the main program,
# tell it to move to a floor of your choice and then back to the bottom floor.

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
        return

    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
        print(f"Floor {self.current_floor}")
        return self.current_floor

    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
        print(f"Floor {self.current_floor}")
        return self.current_floor


elevator1 = Elevator()
elevator1.go_to_floor(10)
elevator1.floor_down()
elevator1.floor_up()
elevator1.go_to_floor(4)
