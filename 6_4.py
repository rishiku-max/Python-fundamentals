import csv

filename = "students.csv"

# Ask how many students to add
n = int(input("How many students do you want to add? "))

records = []

for i in range(n):
    print(f"\nEnter details for student {i+1}:")
    roll = input("Roll number: ")
    name = input("Name: ")
    marks = input("Marks: ")
    records.append([roll, name, marks])

# Append to file
with open(filename, 'a', newline='') as file:
    writer = csv.writer(file)
    # If file was empty, you may want to write header first (but assuming it exists)
    for rec in records:
        writer.writerow(rec)

print(f"\n{n} student records added successfully!")