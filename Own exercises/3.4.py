class Employee:
    total_employees = 0

    def __init__(self, first_name, last_name):
        Employee.total_employees = Employee.total_employees + 1
        self.employee_number = Employee.total_employees
        self.first_name = first_name
        self.last_name = last_name

    def print_information(self):
        print(f"{self.employee_number}: {self.first_name} {self.last_name}")


class HourlyPaid(Employee):

    def __init__(self, first_name, last_name, hourly_pay):
        self.hourly_pay = hourly_pay
        super().__init__(first_name, last_name)

    def print_information(self):
        super().print_information()
        print(f"Hourly pay: {self.hourly_pay}")


class MonthlyPaid(Employee):

    def __init__(self, first_name, last_name, monthly_pay):
        self.monthly_pay = monthly_pay
        super().__init__(first_name, last_name)

    def print_information(self):
        super().print_information()
        print(f"Monthly pay: {self.monthly_pay}")


employees = []
employees.append(HourlyPaid("Viivi", "Virta", 12.35))
employees.append(MonthlyPaid("Ahmed", "Habib", 2750))
employees.append(Employee("Pekka", "Puro"))
employees.append(HourlyPaid("Olga", "Glebova", 14.92))

for e in employees:
    e.print_information()
