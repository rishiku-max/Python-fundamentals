# tuple ordered, immutable, duplicate

a = (10, 20, 30, 40, 50)
a.count(10)

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)
print(len(thistuple))
print(type(thistuple))
print(thistuple[1])
print(thistuple[-1])
print(thistuple[2:5])
print(thistuple[:4])
print(thistuple[2:])
x = thistuple.count("apple")
print(x)
y = thistuple.index(3)
print(y)

