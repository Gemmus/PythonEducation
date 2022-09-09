matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[0][1])

for row in matrix:
    for item in row:
        print(item)
#
number = [4, 7, 7, 37, 97, 98, 54]
number2 = number.copy()     # creates an independent list

number.insert(3, 67)
print(number)
number.remove(98)
print(number)
number.pop()    # deletes the last one from the list
print(number)


print(number.index(37))     # what position in the list

print(98 in number)     # checking if in the list

print(number.count(7))      # how many in the list

number.sort()
print(number)

number.reverse()
print(number)

print(number2)

number.clear()
print(number)
