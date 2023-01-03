import random
#intro statement
print("Enter - Dice Simulator")
# always have x = "y" to run while loop

a = 0
x = a


while x == a:
    number = random.randint(1, 6)
    if number == 1:
        print("===========")
        print("|         |")
        print("|    O    |")
        print("|         |")
        print("===========")

    if number == 2:
        print("===========")
        print("|         |")
        print("| 0     0 |")
        print("|         |")
        print("===========")

    if number == 3:
        print("===========")
        print("| O       |")
        print("|    O    |")
        print("|       O |")
        print("===========")

    if number == 4:
        print("===========")
        print("| 0     0 |")
        print("|         |")
        print("| 0     0 |")
        print("===========")

    if number == 5:
        print("===========")
        print("| 0     0 |")
        print("|    0    |")
        print("| 0     0 |")
        print("===========")
    
    if number == 6:
        print("===========")
        print("| 0     0 |")
        print("| 0     0 |")
        print("| 0     0 |")
        print("===========")
    
    a += 1
    # allows for die to be rolled once
    # Optional Challenge: Implement user input to
    #                     where certain key allows
    #                     die to be rerolled, and
    #                     other keys cause error
    #                     message
