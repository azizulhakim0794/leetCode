# python3 3360_Stone_Removal_Game.py
n = 34

# Output: true

stones = 10
count = 0

while n >= stones:
    n -= stones
    stones -= 1
    count += 1

print(count % 2 == 1)

# for i in range(10, -1,-1):
#             if n < i:
#                 return i%2 != 0
#             n -= i
#         return False



