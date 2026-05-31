# LISTS

# Print only even numbers from list
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for n in nums:
    if n % 2 == 0:
        print(n)



# Replace names starting with vowel
names = ["Aman", "Rishi", "Isha", "Karan", "Om"]

vowels = "aeiouAEIOU"

for i in range(len(names)):
    if names[i][0] in vowels:
        names[i] = "Vowel"

print(names)



# Largest & smallest without max/min
nums = [4, 7, 1, 9, 2]

largest = nums[0]
smallest = nums[0]

for i in nums:
    if i > largest:
        largest = i
    if i < smallest:
        smallest = i

print("Largest:", largest)
print("Smallest:", smallest)



# Common elements from two lists
list1 = list(map(int, input("Enter first list numbers: ").split()))
list2 = list(map(int, input("Enter second list numbers: ").split()))

common = []

for x in list1:
    if x in list2 and x not in common:
        common.append(x)

print(common)