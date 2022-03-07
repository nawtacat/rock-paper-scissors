import random

while True:
    chug = random.randint(1, 3)
    # 1 is rock
    while chug == 1:
        chug = random.randint(1, 3)
        you = input(" Scissors, Rock or Paper? ")
        if you == "Scissors":
            print("You Lost PC was Rock")
        if you == "Rock":
            print("Same Draw")
        if you == "Paper":
            print("PC was Rock, You Won")
    #2 is paper
    while chug == 2:
        chug = random.randint(1, 3)
        you = input(" Scissors, Rock or Paper? ")
        if you == "Scissors":
            print("Congrats the PC Chose Paper")
            print("You Won")
        if you == "Rock":
            print("The PC was Paper You Won")
        if you == "Paper":
            print("Same, Draw")
    #3 is scissors
    while chug == 3:
        chug = random.randint(1, 3)
        you = input(" Scissors, Rock or Paper? ")
        if you == "Scissors":
            print("The Same")
            print("Draw")
        if you == "Rock":
            print("The PC chose Scissors You won")
        if you == "Paper":
            print("You Lost the PC was Scissors")








