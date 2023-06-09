money = int(input("Enter money: "))
r_2000 = money // 2000
money = money % 2000

r_500 = money // 500
money = money % 500

r_200 = money // 200
money = money % 200

r_100 = money // 100
money = money % 100

r_50 = money // 50
money = money % 50

r_20 = money // 20
money = money % 20

r_10 = money // 10
money = money % 10

c_5 = money // 5
money = money % 5

c_2 = money // 2
money = money % 2

c_1 = money // 1
money = money % 1

print("2000 Rs = ",r_2000)
print("500 Rs = ",r_500)
print("200 Rs = ",r_200)
print("100 Rs = ",r_100)
print("50 Rs = ",r_50)
print("20 Rs = ",r_20)
print("10 Rs = ",r_10)
print("5 Rs = ",c_5)
print("2 Rs = ",c_2)
print("1 Rs = ",c_1)