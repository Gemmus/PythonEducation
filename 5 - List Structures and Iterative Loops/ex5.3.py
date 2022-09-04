# Write a program that asks the user for an integer and tells if the number is a prime number.

num = int(input("Please enter an integer number: "))

if num > 1:
    if num == 2:
        print(str(num) + " is a prime number.")
    else:
        n = True
        for i in range(2, num-1):
            if num % i == 0:
                print(str(num) + " is not a prime number.")
                n = False
                break
        if n:
            print(str(num) + " is a prime number.")

else:
    print(str(num) + " is not a prime number.")
