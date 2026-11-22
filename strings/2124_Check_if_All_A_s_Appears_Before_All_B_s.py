# python3 2124_Check_if_All_A_s_Appears_Before_All_B_s.py
s = "aaabbb"
# Output: true
s = "abab"
# s = "bbb"



if 'a' not in s and 'b' not in s:
    print(False)
if 'a' not in s and 'b' in s:
    print(True)
if 'a' in s and 'b' not in s:
    print(True)

a_index = []
b_index = []

for i in range(len(s)):
    if s[i] == 'a':
        a_index.append(i)
    else:
        b_index.append(i)

if a_index[len(a_index)-1] < b_index[0]:
    print(True)
else:
    print(False)
