users = ["shalvi","aaryan","nishi","dev"]
print(users)



users.append("Anisha")
users.extend(["dhruvil","himani","Devang"])
#users.sort()
#users.sort(reverse=True)
#users.reverse()
#users.remove("aaryan")
#users.insert(1,"aaryan")
usercpy = users.copy()
print(usercpy)
count=users.count("aaryan")
print(count)
name =users.index("shalvi")
print(name)
users.pop()
users.clear()
for i in users:
    print(i)