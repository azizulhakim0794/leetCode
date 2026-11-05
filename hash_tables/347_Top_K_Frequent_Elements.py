# python 347_Top_K_Frequent_Elements.py

nums = [4, 1, -1, 2, -1, 2, 3]
k = 2


# def fusnj():
#     count = {}
#     buckets = [[] for _ in range(len(nums) + 1)]
#     # new_arr = []

#     for num in nums:
#         count[num] = count.get(num, 0) + 1

#     for num, freq in count.items():
#         buckets[freq].append(num)

#     k = 2
#     result = []
#     # print(buckets)

#     for i in range(len(buckets) - 1, 0, -1):
#         for num in buckets[i]:
#             result.append(num)

#             if len(result) == k:
#                 break

#             if len(result) == k:
#                 break

#         print(result)

# fusnj()


count = {}
# new_arr = []

for num in nums:
    count[num] = count.get(num, 0) + 1


max_freq = max(count.values())

result = []

new_arr = sorted(count, key=count.get, reverse=True)

print(new_arr[:k])
for num, freq in count.items():
    print(num, freq)
    # buckets[freq].append(num)


# for i in range(5, 0, -2):
#     print(i)
