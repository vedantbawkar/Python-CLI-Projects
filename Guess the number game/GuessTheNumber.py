import random
r = random.randint(1,20010)
# print (r)
g=None
i=0
while (g!=r):
    g = int(input("Enter your guess : "))
    if (g==r):
        print("Your guessed it right!")
        i+=1
    else:
        i+=1
        if (g>r):
            print("You guessed it wrong, enter a smaller number")
        else:
            print("You guessed it wrong, enter a larger number")
print(f"Took you {i} guesses")