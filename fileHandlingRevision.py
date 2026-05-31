# Question 1:


f = open("Marks3.txt", "w")
list1 = []
for i in range(4):
    rollno = int(input("Enter roll no: "))
    name = input("Enter your name: ")
    marks = int(input("Enter your marks: "))
    list1.append({"rollno": rollno,"name": name,"marks": marks})

f.write(str(list1))
f.close()

def display():
    file = open("Marks3.txt", "r")
    print(file.read())
    file.close()
display() 