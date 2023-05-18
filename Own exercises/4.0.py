class Customer:
    number_of_customers = 0

    def __init__(self, first_name, last_name, number_of_loyalty_points):
        Customer.number_of_customers += 1
        self.customer_number = Customer.number_of_customers
        self.first_name = first_name
        self.last_name = last_name
        self.number_of_loyalty_points = number_of_loyalty_points

    def increase(self, loyalty_points):
        self.number_of_loyalty_points += loyalty_points


customer1 = Customer('Mia', 'Fluffins', 2)
customer2 = Customer('Abdul', 'Ammar', 1)

customer1.increase(3)
customer2.increase(2)

print(f"{customer1.customer_number}: {customer1.first_name} {customer1.last_name} has {customer1.number_of_loyalty_points} points.")
print(f"{customer2.customer_number}: {customer2.first_name} {customer2.last_name} has {customer2.number_of_loyalty_points} points.")

print(f"We have in total {Customer.number_of_customers} customers.")
