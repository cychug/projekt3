koniec = 0
while koniec == 0:
    u = input("Uzytkownik podaj p - papier, k - kamień lub n - nozyczki. Inny kończy grę. ")
    if (u == "p") or (u == "k") or (u == "n"):
        m = input("Macbook podaj p - papier, k - kamień lub n - nozyczki. Inny kończy grę. ")
        if (m == "p") or (m == "k") or (m == "n"):
            if (u == "p") and (m == "p"):
                print("remis")
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
        else:
            koniec = 1
    else:
        koniec = 1
print("Koniec gry")
