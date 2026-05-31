# DICTIONARIES
# Students scoring more than 75
students = {"Rishi": 80, "Aman": 60, "Neha": 90}

for name in students:
    if students[name] > 75:
        print(name)

#  Character frequency
text = input("Enter string: ")
freq = {}

for ch in text:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

print(freq)

# Keys whose values are even
d = {"a": 2, "b": 3, "c": 6}

for k in d:
    if d[k] % 2 == 0:
        print(k)

# Update, delete, print dictionary
d = {"pen": 10, "book": 20, "bag": 30, "box": 40, "eraser": 50}

d["book"] = 25      # update
del d["box"]        # delete

print(d)