definicje = {}
while(True):
    print("1: dodaj, 2: znajdz, 3: usuń, 4: koniec")
    wybor = input("Co chcesz zrobić: ")
    if (wybor == "1"):
        klucz = input("Podaj klucz dla przyszłej definicji: ")
        definicja = input("Teraz podaj definicję: ")
        definicje[klucz] = definicja                    # dodanie do słownika element
        print("Definicja została pomyślenie dodana: ", definicje)
    elif (wybor == "2"):
        klucz = input("Czago szukasz? Podaj sam klucz definicji: ")
        if klucz in definicje:
            print("Znalazłem definicję z kluczem: ", klucz, "oraz definicją: ", definicje[klucz])
        else:
            print("Nie znaleziono definicji z kluczem: ", klucz)
    elif (wybor == "3"):
        klucz = input("Co usunąć? ")
        if klucz in definicje:
            del definicje[klucz]                        # usuwanie
            print("Usunięto definicję z kluczem: ", klucz)
        else:
            print("Nie znaleziono definicj z kluczem ", klucz)
    elif (wybor == "4"):
        break
    else:
        print("podałeś cos z poza listy wyboru, spróbuj jeszcze raz")
    print("Słownik wygląda tak: ", definicje)
