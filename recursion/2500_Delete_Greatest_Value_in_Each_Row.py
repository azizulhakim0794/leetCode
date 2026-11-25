# python3 2500_Delete_Greatest_Value_in_Each_Row.py
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


def max_rows_sum(grid=[[]], pre_num=0):

    temp_arr = []
    max_num = pre_num

    if len(grid[0]):
        for row in grid:
            temp_arr.append(max(row))

        max_num+= max(temp_arr)

        for row in grid:
            if max(row) in row:
                row.remove(max(row))
        return max_rows_sum(grid,max_num)

    else:
        return max_num


max_rows_sum(grid)
print(max_rows_sum(grid))
