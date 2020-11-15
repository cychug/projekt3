endGame = 0
while endGame == 0:
    u = input("User - enter a letter p - paper, r - rock or s - scissors, other letter ends the game. ")
    if (u == "p") or (u == "r") or (u == "s"):
        m = input("MacBook - enter a letter p - paper, r - rock or s - scissors, other letter ends the game. ")
        if (m == "p") or (m == "r") or (m == "s"):
            if (u == "p") and (m == "p"):
                print("draw")
            elif (u == "p") and (m == "r"):
                print("u won")
            elif (u == "p") and (m == "s"):
                print("m won")
            elif (u == "r") and (m == "p"):
                print("m won")
            elif (u == "r") and (m == "r"):
                print("draw")
            elif (u == "r") and (m == "s"):
                print("u won")
            elif (u == "s") and (m == "p"):
                print("u won")
            elif (u == "s") and (m == "r"):
                print("m won")
            elif (u == "s") and (m == "s"):
                print("draw")
        else:
            endGame = 1          # the computer chose a different letter which means game over
    else:
        endGame = 1              # the user the chose a different letter which means game over
print("Game Over")
