list1 = ["shalvi","dev","aa","aaryan","monika"]
#list2 = []
#for i in list1:
#    if len(i)>3:
#        list2.append(i)
#
#print(list2)

#comprehension

list2 = [i for i in list1 if len(i)>3]
print(list2)