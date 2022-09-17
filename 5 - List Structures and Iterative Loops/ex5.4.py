# Write a program that asks for the name of five cities (use a for loop).
# Then the program prints out the name of the cities one city per line, in the same order they were put in.

city_list = []

for n in range(0, 5):
    city = input("Please enter the name of a city: ")
    city_list.append(city)

# for n in range(len(city_list)):
#     print(city_list[n])

# or

for n in city_list:
    print(n)
