# stone Paper Scissors game
import random

def gameWin(comp, you):

    if comp == you:
        return None

    elif comp == 's':
        if you == 'p':
            return True
        elif you == 'S':
            return False

    elif comp == 'p':
        if you == 's':
            return False
        elif you == 'S':
            return True

    elif comp == 'S':
        if you == 'p':
            return False
        elif you == 's':
            return True

print("Comp Turn: stone(s) paper(p) or scissor(S) ? ")
randNo = random.randint(1, 3) 
if randNo == 1:
    comp = 's'
elif randNo == 2:
    comp = 'p'
elif randNo == 3:
    comp = 'S'

you = input("Your Turn: stone(s) paper(p) or scissor(S) ?")
a = gameWin(comp, you)

print(f"Computer chose {comp}")
print(f"You chose {you}")

if a == None:
    print("The game is a tie!")
elif a:
    print("You Win!")
else:
    print("You Lose!")

# contributed by Ravi Kumar
