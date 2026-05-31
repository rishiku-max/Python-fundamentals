# r -> raw string
# # f = open(r"D:\Programmes\Python programmes\test.txt", "r")
# f = open("test.txt","w", errors="ignore")
# # f = open("test.txt","r")
# print(f.read())
# #f.close()
# # read line and read lines
# print(f.readlines())

# f = open("test.txt","w")
# c = f.write("my name is Rishi kumar.")


# f = open("test.txt","w")
# list1 = []
# for i in range(5):
#     name = input("enter students name: ")
#     f.write(name)
#     f.write("\n")

# f.close()

# f = open("test.txt","a+")
# list1 = []
# print(f.read())
# for i in range(5):
#     name = input("enter students name: ")
#     list1.append(name + "\n")
# f.writelines(list1)
# print(f.read())
# f.close()

# f = open("test.txt", "r")
# str = " "
# while str:
#     str = f.readline()
#     print(str, end=" ")
# f.close()

# f = open("Marks.txt", "w")
# list1 = []
# for i in range(2):
#     rollno = int(input("Enter roll no: "))
#     name = input("Enter your name: ")
#     age = int(input("Enter your age: "))
#     list1.append({"rollno": rollno,"name": name,"age": age})

# f.write(str(list1))
# f.close()

#with from Marks.txt as f:

import pickle
# # dump() -> 
# # load() ->
# emp1 = {'empno ': 1201, 'name ': "Ansh mehra", 'age ': 24}
# emp2 = {'empno ': 1202, 'name ': "Kansh mehra", 'age ': 25}
# emp3 = {'empno ': 1203, 'name ': "Sansh mehra", 'age ': 23}
# emp_file = open("emp.dat", "wb")
# pickle.dump(emp1, emp_file)
# pickle.dump(emp2, emp_file)
# pickle.dump(emp3, emp_file)
# emp_file.close()

# emp_file = open("emp.dat", "ab")
# stu = {}
# ans = 'y'
# while ans == 'y':
#     rno = int(input("enter roll no"))
#     name = input("enter name")
#     age = int(input("enter age"))
#     stu["Roll no."] = rno
#     stu["Name"] = name
#     pickle.dump(stu, emp_file)
#     ans = input("Do you want more records")

# emp_file.close()

with open("emp.dat", "rb") as e:
    c = pickle.load(e)
    print(c)
    print(e.tell()) # present position of the pointer
    print(e.seek(13))
    print(pickle.load(e))
