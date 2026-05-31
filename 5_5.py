# Program to display text before letter Q

file = open("myfile.info", "r")

text = file.read()

file.close()

result = ""

# Checking each character
for ch in text:
    if ch == "Q":      # stop when Q is found
        break
    result += ch

print("Text before Q is :")
print(result)