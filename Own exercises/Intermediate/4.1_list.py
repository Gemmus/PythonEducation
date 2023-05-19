fruits = ["banana", "apple", "cherry"]
print(fruits)

fruits.append("pineapple")
print(fruits)

fruits.insert(1, "blueberry")
print(fruits)

fruits.pop()
print(fruits)

fruits.remove("cherry")
print(fruits)

fruits.reverse()
print(fruits)

fruits.clear()
print(fruits)

numbers = [3, 9, 2, 81, 23, 16, 0]
new_numbers = sorted(numbers)
print(new_numbers)
print(numbers)

numbers.sort()
print(numbers)

new_numbers = sorted(numbers)
print(new_numbers)

list_of_5zeros = [0] * 5  # Creates a list of 5 zeros
print(list_of_5zeros)

another_list = [1, 2, 3, 4, 5]
concat = list_of_5zeros + another_list
print(concat)

int_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # slicing
a = int_list[1:5]
print(a)
a = int_list[:5]
print(a)
a = int_list[1:]
print(a)
a = int_list[::2]  # step index
print(a)  # [1, 3, 5, 7, 9]
a = int_list[::-2]  # step index
print(a)  # [9, 7, 5, 3, 1]

# to duplicate
vegetables = ["onion", "carrot", "potato"]
indepedent_copy = vegetables.copy()  # or list(vegetables) or vegetables[:]

indepedent_copy.append("cucumber")
print(vegetables)
print(indepedent_copy)

# list comprehension
a = [1, 2, 3, 4, 5, 6]
b = [i * i for i in a]
print(a)
print(b)
