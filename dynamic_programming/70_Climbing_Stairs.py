# python 70_Climbing_Stairs.py


def fibonacci(n, memo={}):
    if n <= 2:
        return n

    if n in memo:
        return memo[n]

    first = fibonacci(n - 1, memo)
    second = fibonacci(n - 2, memo)

    memo[n] = first + second

    print(memo)

    return memo[n]


print(fibonacci(4))
