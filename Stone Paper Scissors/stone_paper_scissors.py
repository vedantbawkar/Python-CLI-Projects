import random

print("STONE PAPER SCISSORS!")

# Taking the number of rounds, user wants to play
rounds = int(input("Enter the number of rounds you want to play : "))

spc = ["stone","paper","scissors"]
print("Enter stone or paper or scissors")
yourScore = 0
compScore = 0
for i in range(rounds):
    # Round number
    print("\nRound",i+1)

    # Taking user input
    u = input("Your turn...       ")
    while u == "":
        print("\nDude, seriously?o_o")
        u = input("Its your turn...       ")

    # Determining computer's turn
    c = random.choice(spc)
    print("Computer's turn...",c)

    # Determining the result
    if u == "stone" and c == "scissors":
        yourScore+=1
        print("You score a point!")
    elif u == "paper" and c == "stone":
        yourScore+=1
        print("You score a point!")
    elif u == "scissors" and c == "paper":
        yourScore+=1
        print("You score a point!")
    elif c == "stone" and u == "scissors":
        compScore+=1
        print("Computer scores a point:(")
    elif c == "paper" and u == "stone":
        compScore+=1
        print("Computer scores a point:(")
    elif c == "scissors" and u == "paper":
        compScore+=1
        print("Computer scores a point:(")
    else:
        print("No one scores a point-_-")

    # Displaying the scoreboard
    print("Scoreboard\nYou\t|   Computer")
    print(yourScore,end="\t|   ")
    print(compScore)

# Displaying the result
if yourScore>compScore:
    print("\n\n\nVICTORY!!!")
elif compScore>yourScore:
    print("\n\n\nDEFEAT:(")
else:
    print("\n\n\ntie-_-")