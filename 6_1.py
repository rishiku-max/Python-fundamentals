import csv

# 1. Writing to CSV file
filename = "employees.csv"

# Open file in write mode
with open(filename, 'w', newline='') as file:
    writer = csv.writer(file)
    
    # Write header
    writer.writerow(["Emp ID", "Name", "Salary"])
    
    # Write some sample records
    writer.writerow(["101", "Amit", "45000"])
    writer.writerow(["102", "Priya", "52000"])
    writer.writerow(["103", "Rahul", "38000"])

print("Data saved in", filename)

# 2. Reading and displaying
print("\nEmployee Records:")
print("-"*40)

with open(filename, 'r') as file:
    reader = csv.reader(file)
    
    # Skip header if you want, or print it
    header = next(reader)  
    print(f"{header[0]:<10} {header[1]:<15} {header[2]:<10}")
    print("-"*40)
    
    for row in reader:
        print(f"{row[0]:<10} {row[1]:<15} {row[2]:<10}")