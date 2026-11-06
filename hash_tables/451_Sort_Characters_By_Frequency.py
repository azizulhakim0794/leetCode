# python 451_Sort_Characters_By_Frequency.py
s = "trussssieeeeee"
# Output: "eert"


count = {}
ans = ""

for char in s:
    count[char] = count.get(char, 0) + 1


for freq in range(max(count.values()), 0, -1):
    for char, value in count.items():
        if value == freq:
            ans += char * value

print(ans)
