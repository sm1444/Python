maths = int(input("Enter maths marks: "))
sci = int(input("Enter science marks: "))
eng = int(input("Enter english marks: "))

total = maths+sci+eng
per = (total/300)*100

if per>=80:
    print("Grade A")
elif per>=70:
    print("Grade B")
elif per>=60:
    print("grade C")
else:
    print("Fail")        