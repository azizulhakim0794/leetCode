# python 2965_Find_Missing_and_Repeated_Values.py
grid = [[9, 1, 7], [8, 9, 2], [3, 4, 6]]
# Output: [2,4]
# Explanation: Number 2 is repeated and number 4 is missing so the answer is [2,4].

count = {}
result = []

for i in range(len(grid)):
    for j in range(len(grid[i])):
        count[grid[i][j]] = count.get(grid[i][j], 0) + 1

for num, frqe in count.items():
    if frqe > 1:
        result.append(num)
        print(num)
total_length = len(count) + len(result)

for i in range(total_length, 0, -1):
    if i not in count:
        result.append(i)

print(count, result)
