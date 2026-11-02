# python 566_Reshape_the_Matrix.py

mat = [[1, 2, 3, 4, 5, 6]]
r = 2
c = 3

# mat = [[1, 2], [3, 4]]
# r = 1
# c = 4
# Output: [[1,2,3,4]]
# r = 2
# c = 4
# Output: [[1,2],[3,4]]

if len(mat) * len(mat[0]) != c * r:
    print(mat)

temp = []
result = []

for i in range(len(mat)):
    for j in range(len(mat[i])):
        temp.append(mat[i][j])
        print(temp)
        lenth = len(temp)

        if lenth == c:
            result.append(temp)
            temp = []


print(result)
