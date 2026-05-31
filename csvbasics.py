# CSV: Comma Seperated Values: 
# even faster than binary
import csv
# def create_writerow():
#     with open("details.csv", "w") as f: # f is a pointer here
#         fobj = csv.writer(f)
#         d = []
#         d = ["Roll_no", "Name", "Age", "Marks"]
#         fobj.writerow(d)
#         record = []
#         while True:
#             # d = ["Roll_no", "Name", "Age", "Marks"]
#             # fobj.writerow(d)
#             Roll_no = input("enter roll no")
#             Name = input("enter name")
#             Age = input("enter age")
#             Marks = input("enter maerks")
#             record.append([Roll_no, Name, Age, Marks])
#             # fobj.writerow([Roll_no, Name, Age, Marks]) # remove to write in bulk
#             choice = int(input("1 - more /n 2 for exit "))
#             if choice == 2:
#                 break
#         fobj.writerows(record)
# create_writerow()

def display():
    with open("details.csv","r", newline="\r\n") as f:
        fobj = csv.reader(f)
        for i in fobj:
            print(i)
display()


def search():
    with open("details.csv","r", newline="\r\n") as f:
        fobj = csv.reader(f)
        flag = 0
        for i in fobj:
            if i[0]=='4':
                print(i)
                flag = 1
                break
        if flag == 0:
            print("search not found")

search()