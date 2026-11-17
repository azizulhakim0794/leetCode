# python 2500_Delete_Greatest_Value_in_Each_Row.py
grid = [[1, 2, 4], [3, 3, 1]]
# Output: 8

sum = 0

# for i in range(len(grid)):
#     max_num = max(grid[i])
#     for j in range(len(grid[i])):
#         if max_num == grid[i][j]:
#             sum += max_num
#             grid[i].pop(grid[i][j])
# nums = [1, 2, 3, 4, 5]

# nums.remove(3)

# print(nums)


def max_rows_sum(grid=[[]]):

    for row in grid:
        print(row)
    # if len(nums1) == 0 or len(nums2) == 0:
    #     return
    # max_num = max(max(nums1), max(nums2))

    # if max_num:
    #     nums1.remove(max(nums1))
    #     nums2.remove(max(nums2))

    #     return max_rows_sum(nums1, nums2)


max_rows_sum(grid)
# print(max_rows_sum(grid))
