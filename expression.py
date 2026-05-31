# Q.1 -> write a regular expression to check ifa string contains only digits(0-9).
import re
text = "12345"
if re.match("^[0-9]+$", text):
    print("Only digits")


# Q.2 -> write a regex pattern to find the word "cat" in a sentence.
import re
sentence = "The quick brown forx jumps over lazy cat."
if re.search(r"\bcat\b", sentence):
    print("Found cat")


# Q.3 -> Write a regular expression to check if a string starts with the letter "A".
import re
name = "Apple"
if re.match("^A", name):
    print("Starts with A")


# Q.4 -> Write a regex to find all spaces in a given string.
import re
text = "Hello World Python"
spaces = re.findall(r"\s", text)
print("Total spaces:", len(spaces))


# Q.5 -> Write a regular expression to check if a string wnds with ".com"
import re
website = "google.com"
if re.search(r"\.com$", website):
    print("Ends with .com")

