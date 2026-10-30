# python 349_Intersection_of_Two_Arrays.py
# nums1 = [4, 9, 5]
# nums2 = [9, 4, 9, 8, 4]
# Output: [9,4]

# nums1 = [1]
# nums2 = [3]
# Output: []

nums1 = [1]
nums2 = [1]
# Output: [1]

ans = []
count = {}
for num in nums1:
    if num in count:
        count[num] += 1
    else:
        count[num] = 1

for num in nums2:
    if num in count and count[num] > 0 and num not in ans:
        ans.append(num)

print(ans)
