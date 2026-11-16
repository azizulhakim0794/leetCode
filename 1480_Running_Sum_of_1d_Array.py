# python 1480_Running_Sum_of_1d_Array.py
nums = [1, 2, 3, 4]
# Output: [1,3,6,10]

sum = 0
result = []

for num in nums:
    sum += num
    result.append(sum)

print(result)
