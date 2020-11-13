print("Gra w papier, kamień, nozyczki. c - kończy grę")
u = "p"
while u != "c":
    u = input("Uzytkownik podaj p - papier, k - kamień lub n - nozyczki.")
    if (u == "p") or (u == "k") or (u == "n"):
        m = input("Macbook podaj p - papier, k - kamień lub n - nozyczki.")
        if (m == "p") or (m == "k") or (m == "n"):
            if (u == "p") and (m == "p"):
                print("Remis")
            elif (u == "p") and (m == "k"):
                print("u wygrał")
            elif (u == "p") and (m == "n"):
                print("m wygrał")
            elif (u == "k") and (m == "p"):
                print("m wygrał")
            elif (u == "k") and (m == "k"):
                print("remis")
            elif (u == "k") and (m == "n"):
                print("u wygrał")
            elif (u == "n") and (m == "p"):
                print("u wygrał")
            elif (u == "n") and (m == "k"):
                print("m wygrał")
            elif (u == "n") and (m == "n"):
                print("remis")
print("Koniec gry")
