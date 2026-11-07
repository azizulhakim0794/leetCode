# python 1260_Shift_2D_Grid.py

# grid = [[3, 8, 1, 9], [19, 7, 2, 5], [4, 6, 11, 10], [12, 0, 21, 13]]
# k = 4
grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
k = 1

# Output: [[9,1,2],[3,4,5],[6,7,8]]

row = len(grid[0])
temp = []
result = []
total = len(grid) * len(grid[0])
k = k % total
without_k_length = total - k


without_k = []
k_th_item = []
all_flat = []


for i in range(len(grid)):
    for j in range(len(grid[i])):
        if len(without_k) < without_k_length:
            without_k.append(grid[i][j])
        else:
            k_th_item.append(grid[i][j])

for num in k_th_item:
    all_flat.append(num)

for num in without_k:
    all_flat.append(num)

for i in range(len(all_flat)):
    temp.append(all_flat[i])

    if len(temp) == row:
        result.append(temp)
        temp = []


print(result)
