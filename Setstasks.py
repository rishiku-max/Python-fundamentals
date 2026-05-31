# SETS



# Union, Intersection, Difference
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print("Union:", a | b)
print("Intersection:", a & b)
print("Difference:", a - b)


# Remove duplicates using set
lst = [1, 2, 2, 3, 4, 4, 5]

new_list = list(set(lst))
print(new_list)



# Check subset
a = {1, 2}
b = {1, 2, 3, 4}

if a.issubset(b):
    print("a is Subset of b")
else:
    print("Not subset")



# Elements in first set but not second
# a = set(input())
# print(a)
# b = set(input())
# print(b)
# print(a.difference(b))



## 
s1 = set(map(int, input("Enter first set: ").split()))
s2 = set(map(int, input("Enter second set: ").split()))

print(s1.difference(b))
