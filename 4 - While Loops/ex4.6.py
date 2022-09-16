# Implement an algorithm for calculating an approximation for the value of pi (π):

# A unit circle (A) has the radius of 1 and is centered at (0,0).
# Corners of the square B: (-1,-1), (1, -1), (1, 1), (-1, 1).

# If a large number of random points are scattered inside the square,
# the fraction of points that fall inside the circle A correlates with
# the fraction of the area of circle A compared to the area of square B. (πr^2/4 = π/4)

# Generate random points (N = 10^6) inside square B.
# Each is tested if it resides inside circle A. (x^2+y^2<1)
# n: total number of points that fall inside circle A.
# n/N≈π/4, therefore π≈4n/N.


import sys
import random

try:
    N = float(input("How many random numbers shall be generated? "))
    if N > 0:
        n = a = 0

        while a < N:
            x = round(random.uniform(-1, 1), 6)
            y = round(random.uniform(-1, 1), 6)
            a += 1
            if x**2+y**2 < 1:
                n += 1

        print(f"The estimated π value is: ", (4*n)/N)
    else:
        print("Generated number can neither be negative nor zero.")

except ValueError:
    print("Input must be a number.")

sys.exit(0)
