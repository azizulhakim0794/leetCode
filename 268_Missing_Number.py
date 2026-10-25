# python 268_Missing_Number.py
nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]

# Output: 8

seen = set(nums)

for i in range(len(nums)):
    if i + 1 not in seen:
        print(i + 1)
