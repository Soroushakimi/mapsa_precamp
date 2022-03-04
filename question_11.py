import random

player = int (input("pls enter a num from 1 to 20 : "))

computer_choice = random.randint(1,20)

for i in range(1,5) :
    player = int (input("pls enter a num from 1 to 20 : "))
    if player == computer_choice :
        print("You Win !")
        break
    elif i == 4 :
        print("Game Over !")
        print(computer_choice)




