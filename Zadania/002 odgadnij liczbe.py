szukana = 40
podawana = 0
while (szukana != podawana):
    podawana = int(input("Podaj liczbę: "))
    if (podawana == szukana):
        print("Odgadłeś", szukana, "=", podawana)
    elif (podawana > szukana):
        print("Podałeś za duza")
    else:
        print("Podałeś za małą")
