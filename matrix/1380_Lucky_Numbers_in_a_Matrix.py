# python 1380_Lucky_Numbers_in_a_Matrix.py

matrix = [[3, 7, 8], [9, 11, 13], [15, 16, 17]]
# Output: [15]
# Explanation: 15 is the only lucky number since it is the minimum in
# its row and the maximum in its column.
min_row = []

for i in range(len(matrix)):
    min_num = min(matrix[i])

    # Find the column index of the minimum number
    col = matrix[i].index(min_num)

    # Find the maximum number in that column
    max_num = []
    for row in range(len(matrix)):
        max_num.append(matrix[row][col])

    if min_num == max(max_num):
        min_row.append(min_num)

print(min_row)
