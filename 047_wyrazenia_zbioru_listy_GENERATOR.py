"""
podzielne przez 7 nie przez 5 od 100 do 470
Liczba podzielna przez 7 to jej wielokrotność: 7, 14, 21, ...
Liczba podzielna przez 5 to jej wielokrotność: 5, 10, 15, 20, ...
"""

# GENERATOR - potem mozemy przechodzić przez te liczy ale nie będziemy mieli zapisanych nigdzie! NIE BĘDZIEMY MOGLI ICH PÓŹNIEJ WYKORZYTAĆ W PROGRAMIE. ONE SĄ CHWILOWE.
zbiorPodzielne7Nie5 = (
    podzielna
    for podzielna in range(1, 100)
    if (podzielna % 7 == 0) and (podzielna % 5 != 0)
)
for podzielna in zbiorPodzielne7Nie5:
    print(podzielna)


# wyraenie zbioru-  GENERATOR ZBIORU - mozemy potem operować na tychm zbiorze, suma, koniunkcja
zbiorPodzielne7Nie5 = {
    podzielna
    for podzielna in range(1, 100)
    if (podzielna % 7 == 0)     # mozna tez tak zapisać - będzie AND z następną linią
    if (podzielna % 5 != 0)
}
print("Zbiór", zbiorPodzielne7Nie5)

# wyraenie listowe - GENERATOR LISTY - moemy potem operować na liście i będziemy mieli jeszcze kolejność
zbiorPodzielne7Nie5 = [
    podzielna
    for podzielna in range(1, 100)
    if (podzielna % 7 == 0) and (podzielna % 5 != 0)
]
print("Lista", zbiorPodzielne7Nie5)






# drugi sposób {} SŁOWNIK
zbiorPodzielne7 = {
    podzielna7: podzielna7 * 7
    for podzielna7 in range(1, 10)
}
print("Podzielne przez 7: ", zbiorPodzielne7)

zbiorPodzielne5 = {
    podzielna5: podzielna5 * 5
    for podzielna5 in range(1, 10)
}
print("Podzielne przez 5: ", zbiorPodzielne5)

# trzeci sposób [] LISTA
zbiorPodzielne7 = [
    podzielna7 * 7
    for podzielna7 in range(1, 10)
]
print("Podzielne przez 7: ", zbiorPodzielne7)

zbiorPodzielne5 = [
    podzielna5 * 5
    for podzielna5 in range(1, 10)
]
print("Podzielne przez 5: ", zbiorPodzielne5)
