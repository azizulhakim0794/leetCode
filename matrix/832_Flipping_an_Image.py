# python 832_Flipping_an_Image.py
image = [[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]]

# Output: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]

temp = []
result = []
new_arr_col = len(image[0])


for i in range(len(image)):
    temp = []
    for j in range(len(image[i])):
        # the last item from the i'th araay
        if image[i][len(image[i]) - 1 - j] == 0:
            temp.append(1)
        else:
            temp.append(0)

    result.append(temp)


print(result)
