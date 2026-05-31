# Program to store student details in marks.txt
# and display the file content

# Number of students
n = int(input("Enter number of students : "))

# Open file in write mode
file = open("marks.txt", "w")

# Taking user input
for i in range(n):
    print("\nEnter details of Student", i + 1)

    roll = input("Enter Roll Number : ")
    name = input("Enter Name : ")
    marks = input("Enter Marks : ")

    # Writing data into file
    file.write(f"Roll No : {roll}, Name : {name}, Marks : {marks}\n")

file.close()

print("\nData successfully stored in marks.txt")

# Reading and displaying file content
print("\nContents of marks.txt :\n")

file = open("marks.txt", "r")

content = file.read()
print(content)

file.close()