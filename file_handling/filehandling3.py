file = open("dictionary.txt","r")

x = file.readlines()


lines = [line.rstrip("\n") for line in x]
#print(lines)

#palindrome words in the list

list2=[]

for i in lines:
    if i == i[::-1]:
        list2.append(i)

print(list2)
#while True:
#    line = file.readline()
#    if line == "":
#        break
#    print(line,end="")