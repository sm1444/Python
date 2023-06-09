l = [["a","b"],["c","d","e"],["f","g","h"]]
print(l[0][1])
l[2].append("s")
rem = l[0].pop()
print(rem)
for i in l:
    for j in i:
        print(j)
    print("--------")