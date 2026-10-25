# python 504_Base_7.py


num = 101

isNagative = False

if num < 0:
    num = abs(num)
    isNagative = True

base = 10
result = ""

if num == 0:
    result = "0"

while num > 0:
    remainder = num % base
    result = str(remainder) + result
    num = num // base

print(result if isNagative == False else f"-{result}")
