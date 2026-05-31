import csv

filename = "students.csv"   # assume file has: Roll,Name,Marks

search_name = input("Enter student name to search: ").strip().title()

found = False

with open(filename, 'r') as file:
    reader = csv.reader(file)
    header = next(reader)   # skip header
  
    print(f"\n{header[0]:<10} {header[1]:<15} {header[2]:<8}")
    print("-"*40)
    
    for row in reader:
        if row[1].strip().title() == search_name:
            print(f"{row[0]:<10} {row[1]:<15} {row[2]:<8}")
            found = True

if not found:
    print("Student not found.")