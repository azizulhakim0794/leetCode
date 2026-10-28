# python 2_pointers_test.py

# nums = [10, 20, 30, 40, 50]

# left = 0
# right = len(nums) - 1

# while left < right:
#     nums[left], nums[right] = nums[right], nums[left]

#     left += 1
#     right -= 1

# print(nums)


# text = "hello"

# Expected output:

# left = 0
# right = len(text) - 1

# while left < right:
#     if text[left] != text[right]:
#         print(False)
#         break
#     left += 1
#     right -= 1

# print(True)


# print(len(text) // 2)


# nums = [1, 3, 4, 6, 8, 10]
# target = 14

# # Expected output:
# # [4, 10]

# left = 0
# right = len(nums) - 1

# while left < right:
#     total = nums[left] + nums[right]

#     if total == target:
#         print(nums[left], nums[right])
#         break

#     if total > target:
#         right -= 1

#     else:
#         left += 1
# python 2_pointers_test.py

# nums = [1, 2, 3, 4]

# Expected output:
# [1, 3, 12, 0, 0]


# left = 0
# right = 0

# while right < len(nums):
#     if nums[right] != 0:
#         nums[left], nums[right] = nums[right], nums[left]
#         left += 1

#     right += 1

# print(nums)


# nums = [0, 1, 0, 3, 12]

# left = 0

# for right in range(len(nums)):
#     # print(nums[right])
#     if nums[right] != 0:
#         nums[left], nums[right] = nums[right], nums[left]
#         left += 1

# print(nums)


# nums = [1, 1, 2, 2, 3, 4, 4, 5]


# new_new = []

# for right in range(len(nums)):
#     if nums[right] not in new_new:
#         new_new.append(nums[right])


# print(new_new)
s = "a-bC-dEf-ghIj"
# Output: "j-Ih-gfE-dCba"


# left = 0
# right = len(arr_stt) - 1

# while left < right:
#     # if arr_stt[left] != "-":
#     if arr_stt[left].isalpha():
#         arr_stt[left], arr_stt[right] = arr_stt[right], arr_stt[left]

#     left += 1
#     right -= 1

# print("".join(arr_stt))


stack = []
arr_stt = list(s)

for char in s:
    if char.isalpha():
        stack.append(char)


for i in range(len(arr_stt)):
    if arr_stt[i].isalpha():
        arr_stt[i] = stack[-1]
        stack.pop()

print("".join(arr_stt))
