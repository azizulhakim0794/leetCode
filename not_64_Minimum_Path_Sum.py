# python 64_Minimum_Path_Sum.py

# grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
# Output: 7


grid = [[1, 2, 3], [4, 5, 6]]
# Output: 12

# grid = [[1, 2], [1, 1]]
# Output: 3

f_sum = 0
s_sum = 0

for i in range(len(grid)):
    for j in range(len(grid[i])):

        firstArr = grid[i][j]
        last_item = len(grid[i]) - 1

        if i == 0:
            f_sum += firstArr

        if i > 0 and last_item == j:
            f_sum += grid[i][len(grid[i]) - 1]

        if j == 0 and i != (len(grid[i]) - 1):
            s_sum += grid[i][j]

        if i == len(grid[i]) - 1 or i != 0:
            s_sum += grid[len(grid[i]) - 1][j]

# print(min(f_sum, s_sum))
