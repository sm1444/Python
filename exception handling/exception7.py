try:
    age = int(input("Enter your age: "))
    if(age<18):
        raise ValueError("To vote your age must be 18 or more")
    
except ValueError as e:
    print(e)

except:
    print("Something went wrong")