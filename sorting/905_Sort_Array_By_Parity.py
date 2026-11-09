# python 905_Sort_Array_By_Parity.py
nums = [3, 1, 2, 4]
# Output: [2,4,3,1]
# Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.

ans = []
odds = []

for num in nums:
    if num % 2 == 0:
        ans.append(num)
    if num % 2 == 1:
        odds.append(num)

for num in odds:
    ans.append(num)

print(ans)
