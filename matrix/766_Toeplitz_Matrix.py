# python 766_Toeplitz_Matrix.py
matrix = [[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]]
# Output: true
# Explanation:
# In the above grid, the diagonals are:
# "[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]".
# In each diagonal all elements are the same, so the answer is True.

for i in range(len(matrix) - 1):
    for j in range(len(matrix[i]) - 1):

        if matrix[i][j] != matrix[i + 1][j + 1]:
            print(False)

print(True)
