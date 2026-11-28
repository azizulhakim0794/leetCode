# python3 883_Projection_Area_of_3D_Shapes.py
# grid = [[1,2],[3,4]]
grid = [[2]]
# Output: 17
# Explanation: Here are the three projections ("shadows") of the shape made with each axis-aligned plane.

top =0
front = 0
side = 0

cols = []

for i in range(len(grid)):
    side+= max(grid[i])
    cols = []
    for j in range(len(grid[i])):
        if grid[i][j] > 0 :
            top+=1
        cols.append(grid[j][i])
    
    front+= max(cols)

print(top, front, side)
        