# python 485_Max_Consecutive_Ones.py
# 1. extract 0 and 1
# 2. count of eatch
# 3. compare and print

# nums = [1, 1, 0, 1, 1, 1]
nums = [0, 0, 0, 1, 1, 0]
# nums = [1, 0, 1, 1, 0, 0, 0]

count_max = 0
temp_count = 0

for i in range(len(nums)):
    if nums[i] == 0:
        count_max = temp_count if temp_count > count_max else count_max
        temp_count = 0

    if nums[i] == 1:
        temp_count += 1


count_max = temp_count if temp_count > count_max else count_max
print(count_max)
