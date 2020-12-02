"""
    Funkcja - to blok kodu do którego mona odwołać się
              w kadej chwili, aby otrzymać poądany przez nas wynik.

    def nazwa_funkcji():
        instrukcja1
        instrukcja2
"""


def wiadomosc_powitalna(imie):              # przesyłamy arument, określamy paramtery, przed i po definicji dajemy dwie linie
    print(imie)


wiadomosc_powitalna("Arku")
wiadomosc_powitalna("Aniu")
wiadomosc_powitalna("Marku")

imiona = ["Maćku", "Kasiu", "Bartku"]       # lista - zostaną wyświetlon po kolei
for osoba in imiona:
    wiadomosc_powitalna(osoba)

imiona = {"Maćku", "Kasiu", "Bartku"}       # zbiór - nie zostanie wyświtlone po kolei
for osoba in imiona:
    wiadomosc_powitalna(osoba)

imiona = ("Maćku", "Kasiu", "Bartku")       # krotka - nie mona zmieniać elementów krotki choć mona się odwoływac do elementów krotki
for osoba in imiona:
    wiadomosc_powitalna(osoba)
