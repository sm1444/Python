users = ["shalvi","aaryan","nishi","dev","dhruvil","anisha"]

def usersfunc():
    name = input("Enter name of user to add: ")
    users.append(name)
    print("Updated list is: ",users)

usersfunc()