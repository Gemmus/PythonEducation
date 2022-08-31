import sys
import random

N = int(input("How many random numbers shall be generated? "))
n = 0
a = 0

while a < N:
    x = round(random.uniform(-1, 1), 6)
    y = round(random.uniform(-1, 1), 6)
    a = a + 1
    if x**2+y**2 < 1:
        n = n + 1

print(f"The estimated π value is: ", {(4*n)/N})

sys.exit(0)
