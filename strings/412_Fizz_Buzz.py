# python3 412_Fizz_Buzz.py
n = 5
# Output: ["1","2","Fizz"]
ans = []

for num in range(1,n+1):
    if num % 3 == 0 and num % 5 == 0:
        ans.append("FizzBuzz")
        continue
    elif num % 3 == 0:
        ans.append("Fizz")
    elif num % 5 ==0 :
        ans.append("Buzz")
    else:
        ans.append(str(num))
        
print(ans)