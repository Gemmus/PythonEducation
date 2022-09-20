# Write an Elevator class that receives the numbers of the bottom and top floors as initializer parameters.
# The elevator has methods go_to_floor, floor_up and floor_down.
# A new elevator is always at the bottom floor.
# If you make elevator h for example the method call h.go_to_floor(5),
# the method calls either the floor_up or floor_down methods as many times as it needs to get to the fifth floor.
# The methods run the elevator one floor up or down and tell what floor the elevator is after each move.
# Test the class by creating an elevator in the main program,
# tell it to move to a floor of your choice and then back to the bottom floor.

class Elevator:
    def __init__(self, bottom=1, top=10, current=1):
        self.bottom = bottom
        self.top = top
        self.current = current

    def go_to_floor(self, floor):
        if self.bottom <= floor <= self.top:
            self.current = floor
        return self.current

    def floor_up(self):
        if self.current < self.top:
            self.current += 1
        return self.current

    def floor_down(self):
        if self.current > self.bottom:
            self.current -= 1
        return self.current


h = Elevator()
print(h.go_to_floor(5))
for i in range(3):
    h.floor_up()
print(h.current)
print(h.floor_down())
print(h.go_to_floor(10))
