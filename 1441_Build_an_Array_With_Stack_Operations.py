# python 1441_Build_an_Array_With_Stack_Operations.py

target = [1, 3]
n = 3
# Output: ["Push","Push","Pop","Push"]

result = []

target_index = 0
for i in range(1, n + 1):
    result.append("Push")

    if i == target[target_index]:
        target_index += 1

        if target_index == len(target):
            break
    else:
        result.append("Pop")


print(result)
