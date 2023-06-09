ranks = {1:"shalvi",2:"mahi",3:"anusha",4:"dhyey"}

print(ranks)

k=ranks.keys()
print(k)

v=ranks.values()
print(v)

items=ranks.items()
print(items)

ranks[78]="rahil"
ranks[3]="daksh"

ranks.update({7:"malav"})
ranks.update({2:"anusha"})

ranks.update({4:"mahi",5:"aaryan"})

removedelm = ranks.pop(2)
print("removing......",removedelm)

removeditem = ranks.popitem()
print("removing....",removeditem)

data = {}
data = data.fromkeys([1,2,3,4],"shalvi")
print("new dict",data)

for k,v in ranks.items():
    print(k,v)