# python 557_Reverse_Words_in_a_String_III.py
s = "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"

ans = ""

if len(s) > 0:

    s = s.split()

    for i in range(len(s)):
        word = s[i]
        n_word = len(word)
        for j in range(n_word):
            ans += (
                word[n_word - (j + 1)] + " "
                if (n_word - 1) == j and i != len(s) - 1
                else word[n_word - (j + 1)]
            )

print(ans)
