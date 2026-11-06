# python 704_Binary_Search.py

nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]
# in = [1, 2, 3, 4, 5, 06, 07, 08, 09, 10, 11]
target = 5

# Expected output: 3


def binary_search(nums, target):

    left = 0
    right = len(nums) - 1

    while left <= right:

        mid = (left + right) // 2

        print(mid)

        if nums[mid] == target:
            return mid

        elif nums[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    return -1


print(binary_search(nums, target))
