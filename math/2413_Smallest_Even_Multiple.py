# python3 2413_Smallest_Even_Multiple.py
n = 6
# Output: 10
# Explanation: The smallest multiple of both 5 and 2 is 10.
from math import gcd
def find_lcm(x,y):
    return x*y // gcd(x,y)
print(find_lcm(2,n))
