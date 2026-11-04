# python 202_Happy_Number.py
n = 19
# Output: true
# Explanation:
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1


# def happy_num(num):
#     nums = []
#     sum = 0

#     if num <= 4:
#         return num

#     for i in str(num):
#         nums.append(int(i))

#     for num in nums:
#         sum += num * num

#     if sum <= 3:
#         return sum

#     return happy_num(sum)


# print(happy_num(5))


# def happy_num(num, memo={}):
#     nums = []
#     sum = 0

#     if num in memo:
#         return memo[num]

#     if num <= 4:
#         return num

#     for i in str(num):
#         nums.append(int(i))

#     for num in nums:
#         sum += num * num

#     if sum <= 3:
#         return sum

#     memo[num] = happy_num(sum, memo)

#     return memo[num]


def happy_num(num, memo={}):
    if num in memo:
        return memo[num]

    if num <= 4:
        return num

    total = 0

    for digit in str(num):
        total += int(digit) * int(digit)

    memo[num] = happy_num(total, memo)

    print(memo)

    return memo[num]


print(happy_num(5))
