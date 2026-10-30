import math

# python 69_Sqrt.py
# Input: x = 8
# Output: 2
# Input: x = 4
# Output: 2  / 2.8284271247461903
x = 1
num = math.sqrt(x)
# num = x / 2
# print(math.floor(num))
# print(num)


def babylonian_square_root(number, tolerance=1e-10):

    if number > -1:

        # Start with an initial guess
        devided = number / 2.0
        better_devie
        while True:
            better_devie = (devided + number / devided) / 2.0

            # Check if the change is smaller than our tolerance level
            if abs(devided - better_devie) < tolerance:
                return better_devie
            devided = better_devie

    return better_devie


print(math.floor(babylonian_square_root(8)))
