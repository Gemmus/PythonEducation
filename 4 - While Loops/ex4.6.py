# Implement an algorithm for calculating an approximation for the value of pi (π):

# A unit circle (A) has the radius of 1 and is centered at (0,0).
# Corners of the square B: (-1,-1), (1, -1), (1, 1), (-1, 1).

# If a large number of random points are scattered inside the square,
# the fraction of points that fall inside the circle A correlates with
# the fraction of the area of circle A compared to the area of square B. (πr^2/4 = π/4)

# Generate random points (N = 10^6) inside square B.
# Each is tested if it resides inside circle A. (x2+y^2<1)
# n: total number of points that fall inside circle A.
# n/N≈π/4, therefore π≈4n/N.

# Write a program that asks how many random points to generate and at the end prints out the approximation of pi.

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
