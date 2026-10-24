# python hash_items.py

nums = [1, 2, 3, 2, 4, 1]

seen = set()
duplicates = set()

for num in nums:
    if num in seen:
        duplicates.add(num)
    else:
        seen.add(num)

if len(duplicates) > 0:
    print(True)
else:
    print(False)


# solid_nums = []
# duplicates = []

# for num in nums:
#     if num in solid_nums:
#         duplicates.append(num)
#     else:
#         solid_nums.append(num)

# print(duplicates)
