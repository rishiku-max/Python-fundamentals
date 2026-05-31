# Question 3

f = open("Marks3.txt","a+")
list1 = []
print(f.read())

rollno = input("enter students roll no: ")
name = input("enter students name: ")
age = input("enter students age: ")

list1.append(rollno)
list1.append(name)
list1.append(age)
f.writelines(list1)
print(f.read())
f.close()