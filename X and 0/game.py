game = " a1 | a2 | a3 \n----+----+----\n b1 | b2 | b3 \n----+----+----\n c1 | c2 | c3 "
print(game)

valid_inputs = ["a1", "a2", "a3", "b1", "b2", "b3", "c1", "c2", "c3"]

a="a1"
xor0 = "X"
while(a in valid_inputs):

    a = input("Enter the spot where you want to mark "+xor0+" : ")
    game = game.replace(a, xor0+" ")
    print("\n"+game)

    if xor0 == "X":
        xor0 = "O"
    elif xor0 == "O":
        xor0 = "X" 