# moduł to plik z kodem; w tym przypadku figury.py

# biblioteka to złoenie kilku modułów

# moduły dzielimy na 3 rodzaje: standardowe, są wymienione w dokumentacji
# takie które moemy zaimporotwać
# oraz takie które tworzymy sami)

import figury

print(figury.poleProstokata(2, 4))


while(True):
    n = input("""Pole jakiej figury policzyć?
    1 - prostokąt,
    2 - kwadrat,
    3 - trójkąt,
    4 - trapez,
    5 - koło.
    Inny wybór kończy program.
    Jakie pole policzyć: """)
    if (n == '1'):
        a = float(input("Podaj długość boku a: "))
        b = float(input("Podaj długość boku b: "))
        print("Pole prostokąta wynosi: ", figury.poleProstokata(a, b))
    elif (n == '2'):
        a = float(input("Podaj długość boku a: "))
        print("Pole kwadratu wynosi: ", figury.poleKwadratu(a))
    elif (n == '3'):
        a = float(input("Podaj długość podstawy trójkąta: "))
        h = float(input("Podaj długość wysokości: "))
        print("Pole trójkąta wynosi: ", figury.poleTrojkata(a, h))
    elif (n == '4'):
        a = float(input("Podaj długość podstawy a: "))
        b = float(input("Podaj długość podstawy b: "))
        h = float(input("Podaj długość wysokości h: "))
        print("Pole trapezu wynosi: ", figury.poleTrapzu(a, b, h))
    elif (n == '5'):
        r = float(input("Podaj promień koła: "))
        print("Pole koła wynosi: ", figury.poleKola(r))
    else:
        break

