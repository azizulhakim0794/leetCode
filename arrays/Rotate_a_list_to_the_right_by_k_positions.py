# 189. Rotate Array
# python Rotate_a_list_to_the_right_by_k_positions.py
# Example: [1, 2, 3, 4, 5], k = 2 → [4, 5, 1, 2, 3]
# Example: [1, 2, 3, 4, 5], k = 3 → [3, 4, 5, 1, 2]

# k = 2
# nums = [1, 2, 3, 4, 5]


# class RotateList:
#     def __init__(self, count, nums):
#         self.count = count
#         self.nums = nums

#     def rotate(self):
#         fixed_list = []
#         result_list = []
#         # print(self.nums[-2])

#         for j in range(len(self.nums)):
#             item = len(self.nums) - (j + k)
#             fixed_list.append(self.nums[item - 1])

#         for i in range(len(self.nums)):
#             item = len(self.nums) - i
#             result_list.append(fixed_list[item - 1])

#         print(result_list)
#         # print(fixed_list)


# callClass = RotateList(k, nums)
# callClass.rotate()


# k = 2
# nums = [-1, -100, 3, 99]


# class RotateList:
#     def __init__(self, count, nums):
#         self.count = count
#         self.nums = nums
#         count = self.count % len(self.nums)
#         print(count)

#     def rotate(self):
#         fixed_list = []
#         for i in range(self.count):
#             fixed_list.append(self.nums[len(self.nums) - i - 1])

#         fixed_list.reverse()

#         for j in range(len(self.nums) - self.count):
#             fixed_list.append(self.nums[j])

#         print(fixed_list)


# callClass = RotateList(k, nums)
# callClass.rotate()


class RotateList:
    def __init__(self, count, nums):
        self.count = count
        self.nums = nums

    def rotate(self):
        n = len(nums)

        if n == 0:
            return

        k = k % n

        # Reverse the entire list
        nums.reverse()

        # Reverse the first k elements
        nums[:k] = reversed(nums[:k])

        # Reverse the remaining elements
        nums[k:] = reversed(nums[k:])
        print(nums)


nums = [1, 2, 3, 4, 5]
callClass = RotateList(3, nums)
callClass.rotate()


# n = len(nums)

# if n == 0:
#     return

# k = k % n

# # Reverse the entire list
# nums.reverse()

# # Reverse the first k elements
# nums[:k] = reversed(nums[:k])

# # Reverse the remaining elements
# nums[k:] = reversed(nums[k:])
# print(nums)
