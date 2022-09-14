# Write a program that asks for the biological gender and hemoglobin value (g/l).
# The program then notifies the user if the hemoglobin value is low, normal or high.

gender = input("Please enter your biological gender (male or female): ").lower()
try:
    if gender == "female":
        hem = float(input("Please enter your hemoglobin value (g/l): "))
        if 117 <= hem <= 155:
            print("Your hemoglobin value is normal.")
        elif hem < 117:
            print("Your hemoglobin value is low.")
        elif hem > 155:
            print("Your hemoglobin value is high.")

    elif gender == "male":
        hem = float(input("Please enter your hemoglobin value (g/l): "))
        if 134 <= hem <= 167:
            print("Your hemoglobin value is normal.")
        elif hem < 134:
            print("Your hemoglobin value is low.")
        elif hem > 167:
            print("Your hemoglobin value is high.")

    else:
        print("Not valid biological gender.")

except ValueError:
    print("Invalid input.")
