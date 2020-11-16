# lista zagniezdzonych list
listaGosci = [['Krzysiek', 45, 'mezczyzna'],
              ['Ania', 46, 'kobieta'],
              ['Hania', 15, 'kobieta']]
print(listaGosci)

print(listaGosci[0])            # wypisze pierwszy cały element listy
print(listaGosci[0][0])         # wypisze pierwszą część pierwszego elementu
print(listaGosci[2][2])         # wypisze trzecią część, trzeciego elementu

listaGosci[0][1] = 50           # zmiana wybranego elementu listy zagniezdzonej
print(listaGosci)

listaGosci.append(['Magda', 34, 'Kobieta'])     # dodanie elementu do listy, mona te dodawać do listy krotek
print("Lista gości z dodaną Magdą", listaGosci)

# lista zagniezdzonych krotek
listaGosciKrotka = [('Krzysiek', 45, 'mezczyzna'),
                    ('Ania', 46, 'kobieta'),
                    ('Hania', 15, 'kobieta')]
print(listaGosciKrotka)

# krotka zagniezdzonych krotek
krotkaGosci = (('Krzysiek', 45, 'mezczyzna'),
               ('Ania', 46, 'kobieta'),
               ('Hania', 15, 'kobieta'))
print(krotkaGosci)

# zbior zagniezdzonych krotek
zbiorGosci = {('Krzysiek', 45, 'mezczyzna'),
              ('Ania', 46, 'kobieta'),
              ('Hania', 15, 'kobieta')}
print(zbiorGosci)
zbiorGosci.add(('Basia', 67, 'kobieta'))        # dodanie jednej krotki do zbioru DO ZBIORU NIE MONA ZROBIĆ APPEND bo nie wiemy gdzie zostanie dodne
print(zbiorGosci)

# sumowanie zbiorów (POWTARZAJĄCE SIĘ ELEMENTY ZOSTANĄ WYSWIETLONE RAZ)
zbiorGosci1 = {('Krzysiek', 45, 'mezczyzna'),
               ('Ania', 46, 'kobieta'),
               ('Hania', 15, 'kobieta')}
zbiorGosci2 = {('Krzysiek', 45, 'mezczyzna'),
               ('A', 46, 'kobieta'),
               ('H', 15, 'kobieta')}
zbiorGosci3 = zbiorGosci1 | zbiorGosci2         # suma zbiorów
print("Zbior gości 3: ", zbiorGosci3)
print("Kot jest w jednym i drugi zbiorze: ", zbiorGosci1 & zbiorGosci2)
