# python 202_Happy_Number.py
n = 19
# Output: true
# Explanation:
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1


def happy(num):
    if num < 9:
        return num
    sum = 0

    while num > 0:
        d = num % 10
        sum += d**2
        num = num / 10
    return happy(sum)


def happy_num(num):
    nums = []
    sum = 0

    if num <= 4:
        return num

    for i in str(num):
        nums.append(int(i))

    for num in nums:
        sum += num * num

    if sum <= 3:
        return sum

    return happy_num(sum)


print(happy(5))

# if happy_num(n) > 1 :
#     return False
# else :
#     return True

# print(happy_num(4))
