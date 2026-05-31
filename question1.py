##str = input("enter your first name")
#print(len(str))

#str1 = "hi i am $ for $ by $ and $99.99"
#print(str1.count("$"))
#indentation--> proper spacing
# nesting is allowed in python


#lists [] and tuples
list1 = [1,2,2,3,73,4,5,6,6,7,9,8,]  # tpe list
#print(len(list1))
# lists are mutable , can be accessed and modifies/ assign

# list slicing --> same rules to strings
# end_idx does not include
# list methods(specific)....functions available to everything like len(), method for list like (append, list.sort etc..)
# list = [1,2,3]
# print(list.sort()) --> return none
# print(list --> now it will print sorted list)
# print doesnot return anything but they modify accr to command.
# sorting allow for charecters and strings
# list.copy()--> make a shallow copy of the list
# # tuples() -> tuples are immutable just like strings... access but cannot modify
# tup = (1)--> tuple || tip = (1,)--> tuple (datatype)
# slicing --> yes
# tuple methods --> index, count
# dicitonaries --> key: value --> pairs,,,, mutable/,, unorderd --> no index
dict1 = {
    "rishi" : 100,
    "gagan" : 100,
    "daksh" : [2,4,6]
}
# print(dict1)
# print(dict1["rishi"])
# dict1["daksh"] = 7  # overwrite
# print(dict1["daksh"])
# dict1["rounak"] = 54
# print(dict1)
# print(dict1["kartavya"])

#null_dict = {} # null dictinary
# nested dictionaries
student = {
    "name" : "rahul kumar",
    "subject" : {
        "phy" : 99,
        "che" : 76
    }
}
# print(student["subject"]["che"])

# methods in dictionaries
# # print(student.keys())
# print(list(student.keys()))
# print(len(list(student.keys())))

# print(list(student.values()))


# print(list(student.items())) #--> in the form of tuples

# pairs = list(student.items())
# print(pairs[0])

# print(student["name"])
# print(student.get("name"))
# print(student["class"])  -> if not available,  error
# print(student.get("class")) -> if not available returns none

# student.update({"city" : "delhi"})
# print(student)




# set in python ----> unique and immutable items....unordered
# IMPORTANT:-> set-> mutable,,, elements are immutable


null_sert = set()    #--> empty set syntax,..
collection = {1,2,3,4,3}
print(collection)

print(len(collection))

# empty_set = {}  # it is a empty a dictionary

# # --> methods for sets

# empty_set = set()
# empty_set.add(7)
# empty_set.add(5)
# empty_set.add("rishi")
# # we can not add lists due to hashing
# # we can add tuples 
# empty_set.clear()  # make the set empty
# empty_set.pop()  # it returns random value
# empty_set.union()
# empty_set.intersection()

values = {
    ("float", 9.0),
    ("int", 9)
}
print(values)
