# Functions
# 1. block of ConnectionAbortedError
# 2. avoids repetition
# 3. returns the value

# Types: 1. user defined, 2. built in functions

# Declaration--> 


# def add():   # function defined
#     print(5+6)

# add()  # calling

# def myname():
#     print("Rishi")

# myname()

# def add(a,b):
   
#     print(a+b)


# a = int(input())
# b = int(input())
# add(a,b)

# s = int(input())
# def sq(s):
#     print(s*s)

# sq(s)

# to input name from user & display

# def mynames(n="No Name"):
#     print(n)
# name = input()
# mynames(name)  # positional arguments
# mynames()


#6.

# def f_name(first_name, l_name="Chopra"):
#     print(first_name + l_name)

# first_name = input()
# l_name = input()
# f_name(first_name, )
# f_name(first_name, l_name)

# 7.

# n = ["Universal", "Serial", "Bus"]
# def list_name(n):
#     for i in n:
#         print(i)

# list_name(n)

# 8. 


# d = {"pen": 10, "book": 20, "bag": 30, "box": 40, "eraser": 50}
# def dict_name(d):
#     for i in d:
#         print(i, d[i])
# dict_name(d)
# postional arguments and keyword arguments
# 8
# def add(a,b,/,*,d):
#     return a+b+c+d
# a = int(input())
# b = int(input())
# c = add(a,b, c =44, d = 22)
# print(c) 

# 9
# a = int(input())
# def add(a):
#     b =  20
#     return(a+b)

# add()
# print(a)
# print(b) -> it gives error because of local variable


# def add():
#     global a
#     a = 20
#     b = 30
#     print(a+b)
# # add()
# # print(a)
# # print(b)
# a = 6000 # gloabal
# add()
# print(a)
 

# lambda -> Inline code, it is function
# a = 20
# b = 25
# c = 15
# d = 90
# C = lambda a,b,c,d: a+b+c+d
# print(C(a,b,c,d))

# square
# c = lambda x : x*x
# print(c(3))


def fact(n):
    if (n==1):
     return 1
    return fact(n-1)*n


res = fact(5)
print(res)



# ese hi
def fun():
   pass