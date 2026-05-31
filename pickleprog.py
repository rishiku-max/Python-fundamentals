import pickle
def create_binary():
    with open("Emp.dat", "wb") as e:
        Emp = []
        while True:
            Empid = input("ENter employee id")
            Empname = input("ENter employee name")
            Empage = input("ENter employee age")
            Emp = [Empid, Empname, Empage]
            pickle.dump(Emp, e)
            choice = int(input("enter 1 for more\n enter 2 for exit"))
            if choice == 2:
                break

create_binary()           
    

# import pickle
def display():
    with open("Emp.dat", "rb") as e:
        Emp = []
        try:
            while True:
                Emp = pickle.load(e)
                print(Emp)
        except EOFError:
            e.close()
display()    
    