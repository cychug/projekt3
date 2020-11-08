wynik = 0
print("Podaj 4 liczby sprawdzę czy są parzyste")
for i in [1, 2, 3, 4]:
    x = int(input("Podaj liczbę: "))
    modulo = x % 2
    print("Modulo liczby ", x, "to: ", modulo)
    if modulo == 0:
        print(x, " jest liczbą parzystą")
    else:
        print(x, " jest liczbą nieparzystą")
