# strings questions

# Q.1
x = "Hello student"
print(x[::-1])



# Q.2
# phrase = input("Enter a phrase: ")

# words = phrase.split()
# initials = ""

# for word in words:
#     initials = initials + word[0]

# initials = initials.upper()

# print("Initials:", initials)



# Q.3
text = input("Enter a line of text: ")

vowels = "aeiouAEIOU"
count = 0
pairs = ""

for i in range(len(text) - 1):
    if text[i] in vowels and text[i + 1] in vowels:
        count = count + 1
        pairs = pairs + text[i] + text[i + 1] + ", "

print("Number of occurrences of two successive vowels:", count)
print(pairs)
