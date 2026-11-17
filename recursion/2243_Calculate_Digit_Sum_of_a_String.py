# python 2243_Calculate_Digit_Sum_of_a_String.py
s = "11111222223"
k = 3
# Output: "135"
# Explanation:
# - For the first round, we divide s into groups of size 3: "111", "112", "222", and "23".
#   ​​​​​Then we calculate the digit sum of each group: 1 + 1 + 1 = 3, 1 + 1 + 2 = 4, 2 + 2 + 2 = 6, and 2 + 3 = 5.
#   So, s becomes "3" + "4" + "6" + "5" = "3465" after the first round.
# - For the second round, we divide s into "346" and "5".
#   Then we calculate the digit sum of each group: 3 + 4 + 6 = 13, 5 = 5.
#   So, s becomes "13" + "5" = "135" after second round.
# Now, s.length <= k, so we return "135" as the answer.


def digit_sum(nums):

    if len(nums) <= k:
        return nums

    k_arr = ""
    count = ""

    for i in range(len(nums)):

        count += nums[i]

        if len(count) == k or i == len(nums) - 1:

            total = 0

            for j in count:
                total += int(j)

            k_arr += str(total)
            count = ""

    return digit_sum(k_arr)


print(digit_sum(s))
