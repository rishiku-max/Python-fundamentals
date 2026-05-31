# Program to append student records in a binary file

import pickle

# Open binary file in append binary mode
file = open("student.dat", "ab")

n = int(input("Enter number of students to append : "))

for i in range(n):
    print("\nEnter details of Student", i + 1)

    roll = int(input("Enter Roll Number : "))
    name = input("Enter Name : ")
    age = int(input("Enter Age : "))
    marks = float(input("Enter Marks : "))

    # Store record as dictionary
    record = {
        "Roll No": roll,
        "Name": name,
        "Age": age,
        "Marks": marks
    }

    # Write record into binary file
    pickle.dump(record, file)

file.close()

print("\nRecords appended successfully in student.dat")