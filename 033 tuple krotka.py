# po zapisaniu do krotki nie mona zmienić jej elementów, nie dajemy nawiasów [] MOŻNA tylko ewentualnie ()
# z krotki trzeba korzytać wtedy, kiedy zmienne do końca sa niezmienialne, komputer rezerwuje sobie tyle ile potrzebuje
# krotka = ('Krzysiek', 45, 'Abacki')

krotka = (1, 42, 12, -4)            # mozna bez nawisów
print(krotka[0])
krotka = 1, 42, 12, 8
print(krotka)

t = (1, 2, 3)
print(len(t))

krotka = ('Krzysiek', 45, 'Abacki')
print(krotka)
number = 5
krotka = tuple(range(number))
