# Program to count vowels and consonants

f = open("sample.txt", "r")
str = f.read()
count = 0
total = 0
for ch in str:
    total+=1
    if ch.lower() in "aeiou":
        count += 1
print(str)
print("vowels = ", count) 
print("consonents = ", total - count)
f.close()