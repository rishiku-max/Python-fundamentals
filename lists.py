# list -> ordered, mutable, duplicate


a = []
type(a)

thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)
print(len(thislist))
print(type(thislist))
print(thislist[1])
print(thislist[-1])
print(thislist[2:5])
print(thislist[:4])
print(thislist[2:])

thislist.append(15)
thislist.append("date")
thislist.extend(["fastfood, junkfood, bakeryfood"])

print(thislist)

thislist.insert(2, "expensive")
thislist.remove("cherry")
thislist.pop(-3)

print(thislist)

thislist.index("apple")
thislist.count("aplpe")
thislist.sort()
print(thislist)
thislist.reverse()
thislist.copy()
thislist.clear()

print(thislist)