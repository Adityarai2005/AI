id=1
empl={}
def add(name,dept):
        global id
        empl[id]={"name":name,"department":dept}
        id+=1
def update(id,name,dept):
    empl[id]={"name":name,"department":dept}
    
def delete(id):
    del empl[id]
def list():
    for i in empl.keys():
        print(f"Employee id is{i},name is{empl[i]['name']},department is {empl[i]['department']}")
#python main function
if __name__=="__main__":
  while True:
    print("1. Add Employee")
    print("2. Update Employee")
    print("3. Delete Employee")
    print("4. List")
    print("0. Exit")
    choice=int(input("Enter your choice:"))
    if choice==1:
       name=input("enter name:")
       dept=input("enter department")
       add(name,dept)
       print(f"Employee id is{id},name is{name},department is {dept}")
    if choice==2:
       id=int(input("enter the id"))
       name=input("enter name:")
       dept=input("enter department")
       update(id,name,dept)
       print(f"Employee id is{id},name is{name},department is {dept}")
    if choice==3:
        id=int(input("enter the id"))
        delete(id)
        print(f"Employee id is{id},name is{name},department is {dept}")
    if choice==0:
        break
    if choice==4:
        list()