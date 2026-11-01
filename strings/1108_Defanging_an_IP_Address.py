# python 1108_Defanging_an_IP_Address.py
ans = ""
address = "1.1.1.1"
for i in range(len(address)):
    if address[i] == ".":
        ans += "[.]"
    else:
        ans += address[i]
    print(ans)
