# python3 1337_The_K_Weakest_Rows_in_a_Matrix.py

mat = [[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]]
mat = [[1,0],[0,0],[1,0]]
k = 3
# Output: [2,0,3]
# Explanation: 
# The number of soldiers in each row is: 
# - Row 0: 2 
# - Row 1: 4 
# - Row 2: 1 
# - Row 3: 2 
# - Row 4: 5 
# The rows ordered from weakest to strongest are [2,0,3,1,4].

count = {}
result = []
ans = []


for i in range(len(mat)):
    count[i] = 0

    for j in range(len(mat[i])):
        if mat[i][j] == 1:
            count[i] += 1

print(count)

for c, freq  in count.items():
        result.append(freq)


for num in sorted(result):
    for index, freq  in count.items():
        if freq == num and index not in ans:
            ans.append(index)
            if len(ans) == k:
                #  return ans
                 print(ans)
