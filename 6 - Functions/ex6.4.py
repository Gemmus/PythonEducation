# Write a function that gets a list of integers as a parameter.
# The function returns the sum of all the numbers in the list.
# For testing, write a main program where you create a list, call the function, and print out the value it returned.

def func(integers):
    return sum(integers)


list1 = [2, 98, 46, 6, 32, 37, 69, 294, 75]
addition = func(list1)
print(addition)

# or


def func(integers):
    return sum(int(n) for n in integers)


list1 = [2, 98, 46, "6", 32, 37, 69, "294", 75]
addition = func(list1)
print(addition)
