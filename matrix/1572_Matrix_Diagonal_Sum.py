# python 1572_Matrix_Diagonal_Sum.py

# mat = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]
# mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
mat = [[5]]
# Output: 25
# Explanation: Diagonals sum: 1 + 5 + 9 + 3 + 7 = 25
# Notice that element mat[1][1] = 5 is counted only once.


sum = 0

for i in range(len(mat)):
    for j in range(len(mat[i])):
        if i == j:
            sum += mat[i][j]
        if j == len(mat[i]) - 1 - i and i != j:
            sum += mat[i][j]


print(sum)
