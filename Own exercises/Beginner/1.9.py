numbers = [5, 2, 5, 2, 2]

for number in numbers:
    print("x" * number)

# or with nested loop:

for x_count in numbers:
    output = ""
    for count in range(x_count):
        output += "x"
    print(output)
