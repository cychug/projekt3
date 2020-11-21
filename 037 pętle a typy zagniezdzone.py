# operacje na listach zagniezdzonych

zbiorGosci1 = {             # zbiór krotek
               ('Krzysiek', 45, 'mezczyzna', 9876543),
               ('Ania', 46, 'kobieta', 82344553),
               ('Hania', 15, 'kobieta', 4567890)
              }

zbiorGosci2 = {             # słownik krotek
               'Arek': ('Krzysiek', 45, 'mezczyzna', 9876543),
               'Krzysiek': ('Ania', 46, 'kobieta', 82344553),
              }           

for imie, wiek, plec, numerTelefonu in zbiorGosci1:
    print("Imię: ", imie)
    print("Wiek: ", wiek)
    print("Płeć: ", plec)
    print("Numer teleonu: ", numerTelefonu)
    print("\n")             # po kazdym print() jest dodany koniec linii, \n zrobi dwa
