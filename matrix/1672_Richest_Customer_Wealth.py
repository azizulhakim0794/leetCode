# python 1672_Richest_Customer_Wealth.py

accounts = [[1, 5], [7, 3], [3, 5]]
# Output: 10
# Explanation:
# 1st customer has wealth = 6
# 2nd customer has wealth = 10
# 3rd customer has wealth = 8
# The 2nd customer is the richest with a wealth of 10.


ans = set()
sum = 0


for i in range(len(accounts)):
    sum = 0
    for j in range(len(accounts[i])):
        sum += accounts[i][j]
    if sum > 0:
        ans.add(sum)

print(max(ans))
