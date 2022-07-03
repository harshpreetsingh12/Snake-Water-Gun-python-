import random
yourwin=0
pcwin=0
life=10
print("-------------------------- Sanke Water Gun Game --------------------------\n")

while(True):
    if life>=1:
        list = ["snake", "water", "gun"]
        choice = random.choice(list)
        print("choose g for gun, s for snake, w for water")
        choose = input()
        if choose=="g":
            life = life - 1
            print(f"Computer choosed {choice}")
            if choice=="snake":
                print("you got 1 point")
                yourwin=yourwin+1
            elif choice == "water":
                print("computer got 1 point")
                pcwin=pcwin+1
            else:
                print("its a tie")
            print(f'Number of lifes left:-->{life} out of 10\n')
        elif choose=="w":
            life = life - 1
            print(f"Computer choosed {choice}")
            if choice=="gun":
                print("you got 1 point")
                yourwin=yourwin+1
            elif choice == "snake":
                print("computer got 1 point")
                pcwin = pcwin + 1
            else:
                print("its a tie")
            print(f'Number of lifes left:-->{life} out of 10\n')
        elif choose=="s":
            life = life - 1
            print(f"Computer choosed {choice}")
            if choice=="water":
                print("you got 1 point")
                yourwin=yourwin+1
            elif choice == "gun":
                print("computer got 1 point")
                pcwin = pcwin + 1
            else:
                print("its a tie")
            print(f'Number of lifes left:-->{life} out of 10\n')
        else:
            print("Wrong input")
    elif life==0:
        if yourwin>pcwin:
            print(f'The Game is finished you win {yourwin} times and Computer wins {pcwin} times So you are the winner.\n')
            print("Congratulationss !!!!!!!!!!!")
        elif yourwin<pcwin:
            print(f'The Game is finished you win {yourwin} times and Computer wins {pcwin} times So Computer is the winner.\n')
            print("Better Luck Next Time")
        print("Press 1 to play again and 2 for exit")
        again=int(input())
        if again==2:
            break
        elif again==1:
            # global life
            life=10
        # break
