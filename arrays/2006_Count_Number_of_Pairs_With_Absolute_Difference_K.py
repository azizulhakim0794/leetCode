# python 2006_Count_Number_of_Pairs_With_Absolute_Difference_K.py

nums = [1, 2, 2, 1]
k = 1
# Output: 4


def return_k(knum):
    ans = 0
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i < j and abs(nums[i] - nums[j]) == knum:
                ans += 1

    print(ans)
    # return 0


return_k(k)
# print(ans)
