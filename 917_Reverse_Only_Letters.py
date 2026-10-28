# python 917_Reverse_Only_Letters.py
s = "a-bC-dEf-ghIj"
# Output: "j-Ih-gfE-dCba"
stack = []
arr_stt = list(s)

for char in s:
    if char.isalpha():
        stack.append(char)


for i in range(len(arr_stt)):
    if arr_stt[i].isalpha():
        arr_stt[i] = stack[-1]
        stack.pop()

print("".join(arr_stt))
