# python 509_Fibonacci_Number.py
n = 2
# Output: 1
# Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.


# def fibonacci(num):
#     if num <= 2:
#         return 1

#     return fibonacci(num - 1) + fibonacci(num - 2)


# print(fibonacci(6))


def fibonacci(n, memo={}):
    if n <= 1:
        return n

    if n in memo:
        return memo[n]

    first = fibonacci(n - 1, memo)
    second = fibonacci(n - 2, memo)

    memo[n] = first + second

    return memo[n]


print(fibonacci(6))
