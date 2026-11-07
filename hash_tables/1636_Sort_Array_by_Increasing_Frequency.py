# python 1636_Sort_Array_by_Increasing_Frequency.py
nums = [1, 1, 2, 2, 2, 3]
# Output: [3,1,1,2,2,2]

count = {}
ans = []
result = []

for num in nums:
    count[num] = count.get(num, 0) + 1


for freq in range(max(count.values()), 0, -1):
    for num, value in count.items():
        if value == freq:
            ans.extend([num] * value)


def sorting(num):
    return (count[num], -num)


result = sorted(nums)

print(result)
