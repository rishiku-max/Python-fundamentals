import csv

filename = "students.csv"

print("Students who scored more than 80 marks:")
print("-"*35)

with open(filename, 'r') as file:
    reader = csv.reader(file)
  
    count = 0
    for row in reader:
        try:
            marks = int(row[2])   # marks is usually 3rd column
            if marks > 80:
                print(row[1])     # name is usually 2nd column
                count += 1
        except:
            continue   # skip bad rows

if count == 0:
    print("No student scored more than 80 marks.")
else:
    print(f"\nTotal: {count} students")