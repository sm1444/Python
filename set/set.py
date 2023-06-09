#to remove duplicate elements of a list
#list1 = [1,2,2,3,3,44]
#list2 = set(list1)
#list1 = list(list2)
#print(list1)

#for i in list1:
#    if(list1.count(i)!=1):
#        list1.remove(i)
#print(list1)

#remove second largest element from a set

set1 = set({44,55,66,77})
set2 = list(set1)

set2.sort()
print("largest element---->",set2[-1])
print("second largest element--->",set2[-2])
