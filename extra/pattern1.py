#rows = 9  # Number of rows in the pattern
#print("0")
#for i in range( rows,0,-1):
#    for j in range(i, 10):
#        print(j,end='')
#    print("0")
#    for k in range(9,0,-1):
#        print(k,end = '')
#    print()

#rows = 10  # Number of rows in the pattern
#
#for i in range(rows):
#    num = rows - i
#    pattern = ""
#    for j in range(i + 1):
#        pattern += str(num)
#        num = (num + 1) % 10
#    for j in range(i):
#        pattern += str(num)
#        num = (num - 1) % 10
#    print(pattern)

#pyramid pattern

for i in range(1,4):
    for j in range(2,0,-1):
        print("",end='')
    print("\n")
for i in range(1,4):
    for j in range(0,3):
        print("*",end='')
    print("\n")