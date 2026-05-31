# Create + Read Binary File and Display Records

import pickle

# ---------- CREATE FILE (student.dat) ----------

file = open("student.dat", "wb")

n = int(input("Enter number of students : "))

for i in range(n):

    print("\nEnter details of Student", i + 1)

    roll = int(input("Enter Roll Number : "))
    name = input("Enter Name : ")
    age = int(input("Enter Age : "))
    marks = float(input("Enter Marks : "))

    record = {
        "Roll No": roll,
        "Name": name,
        "Age": age,
        "Marks": marks
    }

    pickle.dump(record, file)

file.close()

print("\nBinary file created successfully.\n")


# ---------- READ ALL RECORDS ----------

file = open("student.dat", "rb")

print("All Student Records :\n")

try:
    while True:
        record = pickle.load(file)
        print(record)

except EOFError:
    file.close()


# ---------- RECORDS HAVING MARKS > 81 ----------

file = open("student.dat", "rb")

print("\nStudents having Marks greater than 81 :\n")

try:
    while True:
        record = pickle.load(file)

        if record["Marks"] > 81:
            print(record)

except EOFError:
    file.close()