# python base.py


# mid
# Problem 5: Find the Main Diagonal Sum
# Problem 6: Reverse Every Row
# Problem 7: Transpose a Matrix
# Problem 8: Search a Target
# Problem 9: Boundary Traversal
# Problem 10: Spiral Traversal

# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Problem 1: Sum of Each Row
# ans = set()
# sum = 0
# for i in range(len(matrix)):
#     sum = 0
#     for j in range(len(matrix[i])):
#         sum += matrix[i][j]
#     if sum > 0:
#         ans.add(sum)


# Problem 2: Find the Largest Number
largetNum = 0

# for i in range(len(matrix)):
#     sum = 0
#     for j in range(len(matrix[i])):
#         if largetNum < matrix[i][j]:
#             largetNum = matrix[i][j]

# print(largetNum)


# Problem 3: Sum of Each Column
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
ans = []
sum = 0
for i in range(len(matrix)):
    sum = 0
    for j in range(len(matrix[i])):
        count = matrix[j][i]
        sum += count
    if sum > 0:
        ans.append(sum)

print(ans)


# Problem 4: Count Even Numbers

# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# ans = set()
# for i in range(len(matrix)):
#     for j in range(len(matrix[i])):
#         if matrix[i][j] % 2 == 0:
#             ans.add(matrix[i][j])

# print(ans)
