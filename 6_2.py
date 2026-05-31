
import csv

filename = "employees.csv"   # change name if needed

count = 0

with open(filename, 'r') as file:
    reader = csv.reader(file)
    # Skip header row (optional - remove this line if you want to count header too)
    next(reader, None)
    
    for row in reader:
        count += 1

print(f"Total number of records = {count}")