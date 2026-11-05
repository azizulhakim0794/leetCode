# python 1137_N-th_Tribonacci_Number.py
n = 4
# Output: 4
# Explanation:
# T_3 = 0 + 1 + 1 = 2
# T_4 = 1 + 1 + 2 = 4


def tribo(num, memo=None):

    if memo is None:
        memo = {}

    if num in memo:
        return memo[num]

    if num == 2 or num == 3:
        return num - 1

    if num <= 4:
        return num

    memo[num] = tribo(num - 1, memo) + tribo(num - 2, memo) + tribo(num - 3, memo)

    return memo[num]


print(tribo(25))


# def tribo(num, memo=None):
#     if memo is None:
#         memo = {}

#     if num in memo:
#         return memo[num]

#     if num <= 4:
#         return num

#     memo[num] = tribo(num - 1, memo) + tribo(num - 2, memo) + tribo(num - 3, memo)

#     return memo[num]


# print(tribo(25))
