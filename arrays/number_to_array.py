# python number_to_array.py

listItem = (
    1,
    20,
    5,
    6,
    7,
    88,
    23,
    3,
)
y = []

for x in listItem:
    y.append(x)
print(y)

num = 1245678
arr = []
while num > 0:
    arr.append(num % 10)
    num //= 10
print(arr)  # Output: [1, 2, 4, 5, 6, 7, 8]


# print(len(listItem))
