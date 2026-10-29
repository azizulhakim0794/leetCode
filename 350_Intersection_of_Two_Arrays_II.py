# python 350_Intersection_of_Two_Arrays_II.py

nums1 = [1, 2, 2, 1]
nums2 = [2, 2]

# nums1 = [4, 9, 5]
# nums2 = [9, 4, 9, 8, 4]

# Output: [2,2]
# Try writing the Python code using these hints:
# 1. Use {} to create your hash map.
# 2. Use [] to create your result list.
# 3. Use count[num] += 1 to increase a frequency.
# 4. Use count[num] -= 1 when you add a matching number to the result.


ans = []
count = {}

for num in nums1:
    count[num] = count.get(num, 0) + 1


for num in nums2:
    if num in count and count[num] > 0:
        ans.append(num)
        count[num] = count.get(num, 0) - 1


# print(ans)


# print(len(count), count2)

# for i in count:
#     print(count[i])
