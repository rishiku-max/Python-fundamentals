# Qustion 2:

# f = open("test1.txt","w")
# # para = input("Enter a paragraph : ")
# f.write(para)
# f.close()

f = open("test1.txt", "r")
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

# Question 5:
f = open("test1.txt", "r")
str = f.read()
count = 0
total = 0
for ch in str:
    total+=1
    if ch.lower() in "q":
        print(str)
        break
f.close()

