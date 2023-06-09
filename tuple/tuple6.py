players = ([56,75,2,14,17],[78,81,8,17,16])
total1=0
total2=0
for i in range(5):
     total1 = total1+players[0][i]
i=0
for i in range(5):
     total2 = total2+players[1][i]
     
print(total1)
print(total2)

if(total1>total2):
    print("Team 1 wins")
elif(total2>total1):
    print("team 2 wins")
else:
    print("tie")