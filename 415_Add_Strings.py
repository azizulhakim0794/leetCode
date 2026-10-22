# python 415_Add_Strings.py
num2 = "000012"
num1 = "125539"


# def str_to_num(n, n2):
#     digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
#     arrLen = len(n2) if len(n2) > len(n) else len(n)

#     result = []
#     carry = 0
#     for i in range(arrLen):
#         num1 = digits.index(n[i])
#         num2 = digits.index(n2[i])

#         total = num1 + num2 + carry
#         result.append(digits[total % 10])
#         carry = total // 10

#     print(result)


# def fill_length(num1, num2):
#     num1_le = len(num1)
#     num2_le = len(num2)

#     isFirstBig = True if num1_le > num2_le else False

#     diff = abs(num1_le - num2_le)

#     zeros = ""

#     for _ in range(diff):
#         zeros += "0"

#     if isFirstBig:
#         str_to_num(num1, zeros + num2)
#     elif isFirstBig == False:
#         str_to_num(zeros + num1, num2)
#     else:
#         str_to_num(num1, num2)


# fill_length(num1, num2)


def str_to_num(n, n2):
    digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    result = []
    carry = 0

    # Start from the rightmost digit
    for i in range(len(n) - 1, -1, -1):
        num1 = digits.index(n[i])
        num2 = digits.index(n2[i])

        total = num1 + num2 + carry

        result.append(digits[total % 10])
        carry = total // 10

    # Add any remaining carry
    if carry:
        result.append(digits[carry])

    # Reverse and return the result
    return "".join(result[::-1])


def fill_length(num1, num2):
    diff = abs(len(num1) - len(num2))
    zeros = "0" * diff

    if len(num1) > len(num2):
        num2 = zeros + num2
    else:
        num1 = zeros + num1

    return str_to_num(num1, num2)


print(fill_length(num1, num2))  # 579
# print(fill_length("99", "1"))  # 100
# print(fill_length("123", "9"))  # 132
