# python 771_Jewels_and_Stones.py
jewels = "aA"
stones = "aAAbbbb"
# Output: 3

count = 0

for j in range(len(jewels)):
    for i in range(len(stones)):
        if jewels[j] == stones[i]:
            count += 1

print(count)
