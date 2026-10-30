# arr = [1, 2, 3, 4, 5]
# number = 0

# for digit in arr:
#     number = number * 10 + digit

# print(number)


arr = [1, 2, 3, 4, 5, 645, 5, 23, 43, 78]

number = ""

for i in arr:
    number += str(i)

number = int(number)

print(number)
