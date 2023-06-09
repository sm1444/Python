data = set({12,45,67,89,0,12})
print(data)
print(type(data))
data.add(133)
data.update({100,99})

data.update([12])



data.discard(12)

un = data.union({11,12,13})
print("un...",un)

d = data.difference({1,2,89,12,45})
print("d...",d)

si = data.symmetric_difference({1,2,89,12,45})
print("si...",si)


print("subset",data.issubset({67}))
print("superset",data.issuperset({67}))



print("data",data)