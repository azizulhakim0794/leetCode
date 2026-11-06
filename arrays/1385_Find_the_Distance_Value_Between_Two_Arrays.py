# python 1385_Find_the_Distance_Value_Between_Two_Arrays.py
# arr1 = [4, 5, 8]
# arr2 = ([10, 9, 1, 8],)
# d = 2
# Output: 2

arr1 = [2, 1, 100, 3]
arr2 = [-5, -2, 10, -3, 7]
d = 6

count = 0

for num in arr1:
    valid = True

    for x in arr2:
        if abs(num - x) <= d:
            valid = False
            break

    if valid:
        count += 1

print(count)
