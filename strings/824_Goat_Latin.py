# python3 824_Goat_Latin.py
# sentence = "I speak Goat Latin"
sentence = "HZ sg L"
ans  = ""
arra_s = sentence.split(" ")
# Output: "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"

for i in range(len(arra_s)):
        if arra_s[i][0].lower() in 'a,e,i,o,u':
            ans+= arra_s[i] +'m'+ 'a'*(2+i) + ' '
        else:
            fixed_l = ""
            if len(arra_s[i]) > 1:
                fixed_l = arra_s[i][1:-1]+arra_s[i][-1]+arra_s[i][0]
            else:
                fixed_l = arra_s[i][1:-1]+arra_s[i][-1]
            ans+= fixed_l +'m'+ 'a'*(2+i) + (' ' if len(arra_s)-1 != i else '')
            print(len(arra_s[i]))

print(ans)