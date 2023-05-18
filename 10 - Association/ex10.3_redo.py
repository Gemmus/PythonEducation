# Extend the program again by adding a method fire_alarm that does not receive any parameters
# and moves all elevators to the bottom floor.
# Continue the main program by causing a fire alarm in your building.

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

    def fire_alarm(self):
        for i in range(len(self.elevators)):
            self.elevators[i].go_to_floor(0)


building1 = Building(20, 0, 5)
building1.run_elevator(1, 4)
building1.run_elevator(2, 3)
building1.run_elevator(3, 8)
building1.run_elevator(4, 10)
building1.run_elevator(5, 5)

building1.fire_alarm()

