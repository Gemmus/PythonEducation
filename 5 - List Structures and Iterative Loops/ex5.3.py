# Write a program that asks the user for an integer and tells if the number is a prime number.
# Implemented based on the algorithm from wikipedia:
# https://en.wikipedia.org/wiki/Leap_year#/media/File:Leap_Year_Algorithm.png

try:
    num = int(input("Please enter an integer number: "))

    if num > 1:
        if num == 2:
            print(f"{num} is a prime number.")
        else:
            n = True
            for i in range(2, num-1):
                if num % i == 0:
                    print(f"{num} is not a prime number.")
                    n = False
                    break
            if n:
                print(f"{num} is a prime number.")

    else:
        print(f"{num} is not a prime number.")

except ValueError:
    print("Input must be integer number.")
