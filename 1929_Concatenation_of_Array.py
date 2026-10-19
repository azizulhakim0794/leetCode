# python 1929_Concatenation_of_Array.py
nums = [1, 2, 1]
# Output: [1,2,1,1,2,1]

ans = []

for i in nums:
    ans.append(i)

for i in nums:
    ans.append(i)

print(ans)

# ans=nums+nums

# print(nums * 2)
