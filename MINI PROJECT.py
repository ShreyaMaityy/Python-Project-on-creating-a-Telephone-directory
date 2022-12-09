name=["lohith","Anshit","Shreya"]
number=["9682244253","34857934850","3598069834 "]
a=input("please enter the name or number you want to search:- ")
if len(name)==len(number):
    if a in name:
        d = name.index(a)
        print(number[d])
    elif a in number:
        v = number.index(a)
        print(name[v])
    else:
        print("name or number not found")
else:
    ("print lenghth not same")
b=input("do u want to add or change any number or name (yes or no):-")
if b=="yes":
    x=int(input("how many names or numbers you want to add:-"))
    for i in range(0, x):
        addnames = input("enter name:-")
        addnumbers = input("enter number:-")
        name.append(addnames)
        number.append(addnumbers)
    search = input("do you want to search one more time (yes or no):-")
    if search == "yes":
        detail = input("enter name or number:-")
    if detail == "name":
        l1 = input("enter name:-")
        if l1 in name:
            m = name.index(l1)
            print(number[m])
        else:
            print("invalid name")
    if detail == "number":
        l2 = input("enter number:-")
        if l2 in number:
            p = number.index(l2)
            print(name[p])
        else:
            print("invalid number")
d=input("do you want to see the full list of name and numbers:-")
if d=="yes":
    dict1=dict(zip(name,number))
    print(dict1)
else:
    print("Thankyou")









