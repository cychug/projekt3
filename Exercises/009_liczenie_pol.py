import math


def poleProstokata(a, b):
    return(a * b)


def poleKwadratu(a):
    return(a ** a)


def poleTrojkata(a, h):
    return(a * h / 2)


def poleTrapzu(a, b, h):
    return((a + b) * h / 2)


def poleKola(r):
    return(math.pi * r)


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
        print("Pole prostokąta wynosi: ", poleProstokata(a, b))
    elif (n == '2'):
        a = float(input("Podaj długość boku a: "))
        print("Pole kwadratu wynosi: ", poleKwadratu(a))
    elif (n == '3'):
        a = float(input("Podaj długość podstawy trójkąta: "))
        h = float(input("Podaj długość wysokości: "))
        print("Pole trójkąta wynosi: ", poleTrojkata(a, h))
    elif (n == '4'):
        a = float(input("Podaj długość podstawy a: "))
        b = float(input("Podaj długość podstawy b: "))
        h = float(input("Podaj długość wysokości h: "))
        print("Pole trapezu wynosi: ", poleTrapzu(a, b, h))
    elif (n == '5'):
        r = float(input("Podaj promień koła: "))
        print("Pole koła wynosi: ", poleKola(r))
    else:
        break
