#               ele. unikalne   |   kolejność    |  zmiana konkr. elementu  |   nowe elementy
# listy             NIE                 TAK                 TAK                     TAK
# krotki            NIE                 TAK                 NIE                     NIE
# słowniki          TAK                 NIE                 TAK                     TAK
# zbiory            TAK                 NIE                 NIE                     TAK

# listy         imiona = ["Krzysiek", "Ania", "Bartek", "Kuba", "Robert"]
# krotki        krotka = (1, 42, 12, -4)
# słowniki      pokoje = {49: 'Krzysztof Abacki', 69: 'Marek Bebacki'}
# zbiory        A = {1, 4, 20, -4, 20}  BONUS: | (suma zbiorów) & (wspólny) - ^

A = {1, 4, 20, -4, 20, 400}          # elementy powinny być unikalne NIE ZOSTANIE WYŚWIETLONY 20 DWA RAZY
print("Oto zbiór ", A)

A.add(7)                        # dodanie elementu
print("Dodałem element 7 ", A)

B = [1, 4, 20, -4, 20]          # TO JEST LISTA!!!
print("To jest lista B: ", B)
print("To jest zbiór zrobiony zlisty: ", set(B))    # zmieniamy listę w zbiór, który mam TYLKO unikalne elementy
B = set(B)                      # zamiana listy w sbiór (tylko unikalne elementy)
C = {3, 6, 20, -200, 400}
print("Zbiór A ", A)
print("Zbiór B ", B)
print("Zbiór C ", C)
print("Wspólne elementy A i B i C: ", A & B & C)    # wspólne elementy zbiorów (baz)
print("Suma zbiorów A i B: ", A | B)                # suma zbiorów
print("Odejmowanie zioru A - C", A - C)             # odejmowanie zbiorów
