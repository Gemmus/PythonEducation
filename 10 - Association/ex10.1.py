# Write an Elevator class that receives the numbers of the bottom and top floors as initializer parameters.
# The elevator has methods go_to_floor, floor_up and floor_down.
# A new elevator is always at the bottom floor.
# If you make elevator h for example the method call h.go_to_floor(5),
# the method calls either the floor_up or floor_down methods as many times as it needs to get to the fifth floor.
# The methods run the elevator one floor up or down and tell what floor the elevator is after each move.
# Test the class by creating an elevator in the main program,
# tell it to move to a floor of your choice and then back to the bottom floor.

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

    def floor_up(self):
        if self.current < self.top:
            self.current += 1
        print(f"Moving up. Floor {self.current}")
        return

    def floor_down(self):
        if self.current > self.bottom:
            self.current -= 1
        print(f"Moving down. Floor {self.current}")
        return


elevator1 = Elevator()
elevator1.go_to_floor(8)
elevator1.floor_down()
elevator1.floor_up()
elevator1.go_to_floor(4)
