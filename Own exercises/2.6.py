def greet(first_name, last_name):
    print(f"Hello {first_name} {last_name}!")


print("Start")
greet("Tapio", "Turusta")
greet("my little", "cat")   # positional argument: must be filled and order matters
print("Finish")

greet(last_name="Tapio", first_name="kind")     # keyword argument: order does not matter

greet("Tapio", last_name="kindness")       # can be mixed, but only if first is pos. arg.
