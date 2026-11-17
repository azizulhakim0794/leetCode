# python 43_Multiply_Strings.py
num1 = "123"
num2 = "456"
# Output: "56088"

# main_num1 = 0
# main_num2 = 0
# digits = "0123456789"

# for num in num1:
#     main_num1 = (main_num1 * 10) + digits.index(num)

# for num in num2:
#     main_num2 = (main_num2 * 10) + digits.index(num)

# result = main_num1 * main_num2
# str_result = ""

# if result == 0:
#     print("0")

# str_result = ""

# while result > 0:
#     remainder = result % 10
#     result //= 10

#     str_result += digits[remainder]


# print(str_result[::-1])


result = []

if num1 == "0" or num2 == "0":
    print("0")

result = [0] * (len(num1) + len(num2))
print(result)

for i in range(len(num1) - 1, -1, -1):
    for j in range(len(num2) - 1, -1, -1):

        digit1 = ord(num1[i]) - ord("0")
        digit2 = ord(num2[j]) - ord("0")

        print(ord(num1[i]), num1[i], ord("0"))

        product = digit1 * digit2

        p1 = i + j
        p2 = i + j + 1

        total = product + result[p2]

        result[p2] = total % 10
        result[p1] += total // 10

# print("".join(map(str, result)).lstrip("0"))
print(result)
