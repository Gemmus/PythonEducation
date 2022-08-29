import sys
import math

celsius_str = input("Enter celcius: ")
celsius = float(celsius_str)

print(f"The temperature in Celsius: {celsius:8.5f}")
print(f"{'Pi':12s}:{math.pi:10.5f}")
print(f"{'e':12s}:{math.e:10.5f}")
print(math.e)
print(math.pi)

sys.exit(0)
