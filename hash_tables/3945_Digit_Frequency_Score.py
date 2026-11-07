# python 3945_Digit_Frequency_Score.py
n = 122

# Output: 5
count = {}
str_n = str(n)
sum = 0

for num in str_n:
    count[int(num)] = count.get(int(num), 0) + 1


for num, frqe in count.items():
    sum += num * frqe


print(sum)


# ans = 0

# while n > 0:
#     ans +=  n % 10
#     n //= 10

# return ans
