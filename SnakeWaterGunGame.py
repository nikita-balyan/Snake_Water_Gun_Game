import random
computer=random.choice([-1, 0, 1])
your_choice=input("enter your choice: ")
your_dict={"s":1, "w":-1, "g":0}
reverseDict={1:"s", -1:"w", 0:"g"}

you=your_dict[your_choice]
print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

if(computer == you):
    print("Its a draw")

else:
    if(computer==-1 and you==1):
        print("You win!")
    elif(computer==-1 and you==0):
        print("You lose!")
    elif(computer==1 and you==-1):
        print("You lose!")
    elif(computer==1 and you==0):
        print("You win!")
    elif(computer==0 and you==-1):
        print("You win!")
    elif(computer==0 and you==1):
        print("You lose!")
    else:
        print("Something went wrong!")