import datetime
from datetime import datetime

print("Welcome to health management")


def time():
    now = datetime.now()
    a = now.strftime("%H:%M:%S")
    return a
x=5
while x!=0:
   print("Client code:Romil:1,Shailesh:2,Dishant:3")
   a=int(input("Enter code"))
   if a==1:
    b=int(input("Press 1 for food,2 for excersize"))
    if b==1:
        c=input("Enter food")
        Rf = open('Romil_food.txt', "a")
        Rf.write('%s %s'%(time(), c))
        Rf.write("\n")
        Rf.close()
        x=int(input("Press 0 to end,Press 1 to continue"))
    elif b==2:
        c = input("Enter Exersize")
        Re = open('Romil_exer.txt', "a")
        Re.write('%s %s'%(time(), c))
        Re.write("\n")
        Re.close()
        x = int(input("Press 0 to end,Press 1 to continue"))
    else:
        print("Wrong entry")
        x = int(input("Press 0 to end,Press 1 to continue"))

   if a==2:
    b=int(input("Press 1 for food,2 for excersize"))
    if b==1:
        c = input("Enter food")
        Sf = open('Shailesh_food.txt', "a")
        Sf.write('%s %s'%(time(), c))
        Sf.write("\n")
        Sf.close()
        x = int(input("Press 0 to end,Press 1 to continue"))
    elif b==2:
        c = input("Enter Exersize")
        Se = open('Shailesh_exer.txt', "a")
        Se.write('%s %s'%(time(), c))
        Se.write("\n")
        Se.close()
        x = int(input("Press 0 to end,Press 1 to continue"))
    else:
        print("Wrong entry")
        x = int(input("Press 0 to end,Press 1 to continue"))

   if a==3:
    b=int(input("Press 1 for food,2 for excersize"))
    if b==1:
        c = input("Enter food")
        Df = open('Dishant_food.txt', "a")
        Df.write('%s %s'%(time(), c))
        Df.write("\n")
        Df.close()
        x = int(input("Press 0 to end,Press 1 to continue"))
    elif b==2:
        c = input("Enter Exersize")
        De = open('Dishant_exer.txt', "a")
        De.write('%s %s'%(time(), c))
        De.write("\n")
        De.close()
        x = int(input("Press 0 to end,Press 1 to continue"))
    else:
        print("Wrong entry")
        x = int(input("Press 0 to end,Press 1 to continue"))



