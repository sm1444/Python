#twin number
num = 123
mul = 1
sum = 0
rem = 0
while num>0:
    rem = num %10
    sum = sum + rem
    mul = mul * rem
    num = num//10

if (sum==mul):
    print("twin number")
else:
    print("Not twin number")