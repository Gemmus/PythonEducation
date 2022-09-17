# Write a function that uses a list of integers as its parameters.
# The function returns a second list
# that is otherwise the same as the original list except that all uneven numbers have been removed.
# For testing, write a main program where you create a list, call the function,
# and then print out both the original and the cut-down list.


def func(integers):
    list2 = []
    for integer in integers:
        if integer % 2 == 0:
            even = integer
            list2.append(even)
    print("The even numbers from the original list:", list2)
    return


list1 = [514, 697, 2, 98, 313, 46, 6, 32, 37, 69, 294, 75, 456, 1065, 73, 17]
list1.sort()
func(list1)
