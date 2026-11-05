# python 3345_Smallest_Divisible_Digit_ProductI.py
n = 10
t = 2

# Output: 16

# Explanation:

# The digit product of 16 is 6, which is divisible by 3, making it the smallest
# number greater than or equal to 15 that satisfies the condition.

# num = 15
# arr = []
# total = 1
# while num > 0:
#     arr.append(num % 10)
#     total *= num % 10
#     num = num // 10
# print(arr, total)


def find_product(num):

    reserv_num = num
    total = 1

    while num > 0:
        total *= num % 10
        num = num // 10

    if total % t != 0:
        return find_product(reserv_num + 1)

    return reserv_num


print(find_product(n))
