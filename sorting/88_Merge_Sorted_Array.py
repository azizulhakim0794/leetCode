# python 88_Merge_Sorted_Array.py

nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3

# nums1 = [0]
# m = 0
# nums2 = [1]
# n = 1

ansList = []

for i in range(len(nums1[0:m])):
    ansList.append(nums1[i])

for i in range(len(nums2[0:n])):
    ansList.append(nums2[i])

nums1[:] = sorted(ansList)

print(sorted(ansList))
print(nums1)
