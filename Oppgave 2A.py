# Okei... bare 0-100... ikke noe valg av terninger eller noe?! #sadday
import random as rnd


def roll_for_loot():
    top = "0==================0"
    side = "|                  |"
    roll = rnd.randint(0, 100)
    dice = [top,side,side,"|      ROLLED:     |",f"|{roll:^18}|",side,side,top]
    return "\n".join(dice)

def continous_dice():
    stop = False
    while not stop:
        print(roll_for_loot())
        go_again = input("Enter any key to continue, q to quit!: ")
        if go_again == "q":
            stop = True
    print("Goodbye!")

continous_dice()


"""
=====================================================
Kjøreeksempel:
=====================================================
0==================0
|                  |
|                  |
|      ROLLED:     |
|        97        |
|                  |
|                  |
0==================0
Enter any key to continue, q to quit!: 
0==================0
|                  |
|                  |
|      ROLLED:     |
|        70        |
|                  |
|                  |
0==================0
Enter any key to continue, q to quit!: 
0==================0
|                  |
|                  |
|      ROLLED:     |
|        33        |
|                  |
|                  |
0==================0
Enter any key to continue, q to quit!: 
0==================0
|                  |
|                  |
|      ROLLED:     |
|        86        |
|                  |
|                  |
0==================0
Enter any key to continue, q to quit!: 
0==================0
|                  |
|                  |
|      ROLLED:     |
|        78        |
|                  |
|                  |
0==================0
Enter any key to continue, q to quit!: 
0==================0
|                  |
|                  |
|      ROLLED:     |
|        5         |
|                  |
|                  |
0==================0
Enter any key to continue, q to quit!: q
Goodbye!

Process finished with exit code 0
"""
