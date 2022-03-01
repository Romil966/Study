#Snake water gun game
import random
list=['s','w','g']
u=0
c=0
i=1
while i<=10:
    print(f"Your point{u}")
    print(f"Computer point{c}")
    print(f"Round {i}")
    a=input("Select s/w/g")
    if a=='s' or a=='w' or a=='g':
        b=random.choice(list)
        if a=='s' and b=='g':
            c=c+1
            print("You loose")
            i=i+1
        elif a=='s' and b=='w':
            u=u+1
            print("You win")
            i=i+1
        elif a=='s' and b=='s':
            print("Draw")
            i=i+1
        elif a == 'g' and b == 'g':
            print("Draw")
            i = i + 1
        elif a == 'g' and b == 'w':
            c = c + 1
            print("You loose")
            i = i + 1
        elif a == 'g' and b == 's':
            u = u + 1
            print("You win")
            i = i + 1
        elif a == 'w' and b == 'g':
            u = u + 1
            print("You win")
            i = i + 1
        elif a == 'w' and b == 'w':
            print("Draw")
            i = i + 1
        elif a == 'w' and b == 's':
            c = c + 1
            print("You loose")
            i = i + 1

    else:
        print("wrong entry")
print("Game over")
print(f"Your point:{u}")
print(f"Computer point:{c}")
if u>c:
    print("Congratulations!! You Win")
elif u<c:
    print("You loose")
else:
    print("Match draw")