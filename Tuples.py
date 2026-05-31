# TUPLES
# Tuple → list → add elements → tuple
t = (1, 2, 3)

lst = list(t)
lst.append(4)
lst.append(5)

t = tuple(lst)
print(t)

# Count occurrences in tuple
t = (1, 2, 3, 2, 4, 2)
x = int(input("Enter element: "))

count = 0
for i in t:
    if i == x:
        count += 1

print(count)

# Find index in tuple
t = (10, 20, 30, 40)
x = int(input("Enter element: "))

for i in range(len(t)):
    if t[i] == x:
        print("Index:", i)
        break

# Average of 5 student marks
marks = (80, 75, 90, 85, 70)

total = 0
for m in marks:
    total += m

avg = total / len(marks)
print("Average:", avg)