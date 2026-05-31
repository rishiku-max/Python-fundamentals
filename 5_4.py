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