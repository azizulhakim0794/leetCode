# python 867_Transpose_Matrix.py

# Example 1:
#
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Output: [[1,4,7],[2,5,8],[3,6,9]]


# matrix = [[1, 2, 3], [4, 5, 6]]
# Output: [[1,4],[2,5],[3,6]]


temp = []

result = []

new_arr_row = len(matrix[0])
new_arr_col = len(matrix)

for i in range(len(matrix[0])):
    temp = []
    # print(i, matrix[0][i])
    for j in range(len(matrix)):
        temp.append(matrix[j][i])
        print(matrix[i][j], matrix[j][i])

        if len(temp) == new_arr_col:
            result.append(temp)


print(result)


# for i in range(len(matrix)):
#     j = 0
#     while j < len(matrix[i]):
#         if j >= new_arr_col:
#             j = j - 1
#         temp.append(matrix[j][i])
#         print(matrix[j][i])

#         if len(temp) == new_arr_col:
#             result.append(temp)
#             temp = []
#         j += 1


# print(result)
