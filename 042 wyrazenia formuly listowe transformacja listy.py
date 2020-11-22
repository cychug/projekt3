# stworzenie nowej listy na podstawie starej. Wyrazelnie listowne jest SZYBSZE!!!
# od razu zwróci nam listę
# range (20) - od 0 do 19

liczby = [1, 2, 3, 4, 5, 6]

# NOWY SZYBSZY SPOSOB
potegiDwojki1 = [element ** 2 for element in liczby]
print(potegiDwojki1)

# stary sposób
potegiDwojki = []
for element in liczby:
    potegiDwojki.append(element ** 2)
print(potegiDwojki)

# NOWY SZYBSZY SPOSOB
liczbyParzyste1 = [element for element in liczby if (element % 2 == 0)]
print(liczbyParzyste1)

# stary sposób
liczbyParzyste = []
for element in liczby:
    if (element % 2 == 0):
        liczbyParzyste.append(element)
print(liczbyParzyste)

print()
potegiDwojki2 = [element ** 2 for element in range(5)]
print(potegiDwojki2)
