# python 2319_Check_if_Matrix_Is_X_Matrix.py

grid = [[2, 0, 0, 1], [0, 3, 1, 0], [0, 5, 2, 0], [4, 0, 0, 2]]


# Output: true
def checkXMatrix(self, grid: list[list[int]]) -> bool:

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if i == j:
                if grid[i][j] == 0:
                    return False
            if j == len(grid) - 1 - i:
                if grid[i][j] == 0:
                    return False

            if j != len(grid) - 1 - i and i != j:
                if grid[i][j] > 0:
                    return False

    return True
