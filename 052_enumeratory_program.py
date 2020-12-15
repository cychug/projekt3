# enumeration - spis - wyliczenie
# przy enumeracji dajemy duze litery
# zwięskszenie czytelności
# mniej błędów
# zastosuj zawsze gdy uzytkownik ma coś wybrać : kolor, dni tygodnia.

from enum import IntEnum
import figury

Menu_Figury = IntEnum('Menu_Figury', 'Prostokat, Kwadrat, Trojkat, Trapez, Kolo')   # enumerata
print(list(Menu_Figury))        # wydrukuje wszystkie pozycje z listy i ich numerki
print(Menu_Figury)              # wydrukje tylko to: <enum 'Menu_Figury'>


while(True):
    n = int(input("""Pole jakiej figury policzyć?
    1 - prostokąt,
    2 - kwadrat,
    3 - trójkąt,
    4 - trapez,
    5 - koło.
    Inny wybór kończy program.
    Jakie pole policzyć: """))
    if (n == Menu_Figury.Prostokat):
        a = float(input("Podaj długość boku a: "))
        b = float(input("Podaj długość boku b: "))
        print("Pole prostokąta wynosi: ", figury.poleProstokata(a, b))
    elif (n == Menu_Figury.Kwadrat):
        a = float(input("Podaj długość boku kwadratu: "))
        print("Pole kwadratu wynosi: ", figury.poleKwadratu(a))
    elif (n == Menu_Figury.Trojkat):
        a = float(input("Podaj długość podstawy trójkąta: "))
        h = float(input("Podaj długość wysokości: "))
        print("Pole trójkąta wynosi: ", figury.poleTrojkata(a, h))
    elif (n == Menu_Figury.Trapez):
        a = float(input("Podaj długość podstawy a: "))
        b = float(input("Podaj długość podstawy b: "))
        h = float(input("Podaj długość wysokości h: "))
        print("Pole trapezu wynosi: ", figury.poleTrapzu(a, b, h))
    elif (n == Menu_Figury.Kolo):
        r = float(input("Podaj promień koła: "))
        print("Pole koła wynosi: ", figury.poleKola(r))
    else:
        break

"""
# LISTA
Menu_Figury = IntEnum('Menu_Figury', ['Prostokat', 'Kwadrat', 'Trojkat', 'Trapez', 'Kolo'])

# SŁOWNIK
Menu_Figury = IntEnum('Menu_Figury', {'Prostokat':6, 'Kwadrat':5, 'Trojkat':4, 'Trapez':3, 'Kolo':2})
print(list(Menu_Figury))


print(Enum('Menu_Figury', 'Prostokat Kwadrat Trójkat Trapz Kolo'))    # to jest spis, któremu przypusje się kolejne wartości
# <enum 'Menu_Figury'>
print(list(Enum('Menu_Figury', 'Prostokat Kwadrat Trójkat Trapz Kolo')))   # to jest lista z przypisanymi wartościami
# [<Menu_Figury.Prostokąt: 1>, <Menu_Figury.Kwadrat: 2>, <Menu_Figury.Trójkąt: 3>, <Menu_Figury.Trapz: 4>, <Menu_Figury.Koło: 5>]
"""
