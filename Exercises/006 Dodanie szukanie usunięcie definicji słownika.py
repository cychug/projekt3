definicje = {}
while(True):
    print("1: dodaj")
    print("2: znajdź")
    print("3: usuń")
    print("4: zakończ")
    wybor = input("Co chcesz zrobić: ")
    if (wybor == "1"):
        klucz = input("Podaj klucz (słowo) do zdefiniowania: ")
        definicja = input("Podaj definicję: ")
        definicje[klucz] = definicja                    # dodanie do słownika element
        print("Definicja dodana pomyślenie: ", definicje)
    elif (wybor == "2"):
        klucz = input("Czago szukasz? ")
        if klucz in definicje:
            print(definicje[klucz])
        else:
            print("Nie znaleziono definicji o nazwie: ", klucz)
    elif (wybor == "3"):
        klucz = input("Co usunąć? ")
        if klucz in definicje:
            del definicje[klucz]                        # usuwanie
            print("Usunięto klucz: ", klucz)
        else:
            print("Nie znaleziono definicj o nazwie ", klucz)
    elif (wybor == "4"):
        break
    else:
        print("podałeś cos z poza zakresu")
