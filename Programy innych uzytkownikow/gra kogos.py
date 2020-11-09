import math

print ("Witamy w programie obliczającym pola powierzchni figur!")
 
def p_prostokata (a, b):
    return a*b
def p_kwadratu (a):
    return a**2
def p_trojkata (a, h):
    return (a*h)/2
def p_trapezu (a, b, h):
    return ((a+b)*h)/2
def p_kola (r):
    return math.pi*(r**2)
 
while True:
 
    print ("Wybierz:")
    print ("1, jeśli chcesz obliczyć pole prostokąta")
    print ("2, jeśli chcesz obliczyć pole kwadratu")
    print ("3, jeśli chcesz obliczyć pole trójkąta")
    print ("4, jeśli chcesz obliczyć pole trapezu")
    print ("5, jeśli chcesz obliczyć pole koła")
    print ("6, jeśli chcesz zakończyć program")
    print("\n")
 
    wybor = input("To jakie działanie wykonujemy? ")
 
    if wybor == "1":
        a = int (input("Podaj długość krótszego boku prostokąta: "))
        b = int (input("Podaj długość dłuższego boku prostokąta: "))
        print ("Pole powierzchni prostokąta o bokach",a,"i",b,"wynosi: ",p_prostokata(a,b))
        print ("\n")
    elif wybor == "2":
        a = int (input("Podaj długość boku kwadratu: "))
        print ("Pole powierzchni kwadratu o boku",a,"wynosi: ",p_kwadratu(a))
        print ("\n")
    elif wybor == "3":
        a = int (input("Podaj długość podstawy trójkąta: "))
        h = int (input("Podaj długość wysokości trójkąta: "))
        print ("Pole powierzchni trójąta o podstawie",a,"i wysokości",h,"wynosi: ",p_trojkata(a,h))
        print ("\n")
    elif wybor == "4":
        a = int (input("Podaj długość górnej podstawy trapezu: "))
        b = int (input("Podaj długość górnej podstawy trapezu: "))
        h = int (input("Podaj długość wysokości trapezu: "))
        print ("Pole powierzchni trapezu o podstawach",a,"oraz",b,"i wysokości",h,"wynosi: ",p_trapezu(a,b,h))
        print ("\n")
    elif wybor == "5":
        r = int (input("Podaj długość promienia koła: "))
        print ("Pole powierzchni koła o promieniu",r,"wynosi: ",p_kola(r))
        print ("\n")
    elif wybor == "6":
        print ("\n","Do widzenia! :)","\n")
        break
    else:
        print ("\n","Wybrana opcja nie istnieje! Wybierz którąś z poniższych.","\