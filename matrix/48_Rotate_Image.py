# python 48_Rotate_Image.py

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]]

# ans = []
# result = []
# for i in range(len(matrix)):
#     ans = []
#     for j in range(len(matrix[i])):

#         ans.append(matrix[len(matrix) - 1 - j][i])

#     result.append(ans)

# matrix[:] = result

# print(matrix)


n = len(matrix)

# Transpose
for i in range(n):
    for j in range(i + 1, n):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

# Reverse each row
# for row in matrix:
#     row.reverse()

print(matrix)
