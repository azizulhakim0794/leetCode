# python 3033_Modify_the_Matrix.py
matrix = [[1, 2, -1], [4, -1, 6], [7, 8, 9]]
# Output: [[1,2,9],[4,8,6],[7,8,9]]

ans = []

count = {}

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        count[j] = count.get(j, [])
        count[j].append(matrix[i][j])


for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == -1:
            matrix[i][j] = max(count.get(j))


print(matrix)
