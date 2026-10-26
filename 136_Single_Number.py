# python 136_Single_Number.py


nums = [4, 1, 2, 1, 2]

# Output: 1

count = {}

for num in nums:
    if num in count:
        count[num] += 1
    else:
        count[num] = 1

print(count)

for i in range(len(nums)):
    item = count[nums[i]]
    if item == 1:
        print(nums[i])
        break
