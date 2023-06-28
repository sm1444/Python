class file:
    
    def store_data(self):
        file1 = open("student.txt","r+")
        Student_name = input("Enter name: ")
        grade = int(input("Enter grade: "))
        marks = float(input("Enter marks: "))
        attendence = bool(input("Enter absent or present: "))
        file1.writelines([Student_name,"\n" , str(grade),"\n" , str(marks),"\n" , str(attendence),"\n"])

    def read_data(self):
        file1 = open("student.txt","r+")
        x=file1.readlines()
        lines = [line.rstrip("\n") for line in x]
        print(lines)
        
        

f1 = file()
f1.store_data()
f1.read_data()