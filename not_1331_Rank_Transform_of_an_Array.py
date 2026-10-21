# python 1331_Rank_Transform_of_an_Array.py
# arr = [40, 10, 20, 30]
# Output: [4,1,2,3]

arr = [37, 12, 28, 9, 100, 56, 80, 5, 12]
# Output: [5,3,4,2,8,6,7,1,3]

sort_arr = sorted(arr)

print(sort_arr)

ans = []

for i in range(len(arr)):
    arr_item = arr[i]
    for j in range(1, len(arr)):
        sort_arr_item = sort_arr[j]
        if arr_item == sort_arr_item:
            ans.append(j)

print(sorted(ans))
print(ans)
