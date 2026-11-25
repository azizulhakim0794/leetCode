# python3 1979_Find_Greatest_Common_Divisor_of_Array.py
nums = [7,5,6,8,3]
# Output: 2

min_num = min(nums)
max_num = max(nums)

max_count = 0

for i in range(1, min_num+1):
    if max_num%i == 0 and min_num%i == 0:
        max_count = max(max_count, i)

print(max_count)