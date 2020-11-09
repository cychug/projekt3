import random
listaLiczb = []
 
liczby = [numbers
          for numbers in range(1,50)
          ]
 
 
x = 0
 
while x < 100:
    print("Podaj liczby od 1-50")
    yourNumber = int(input("Podaj pierwszą Liczbę:"))
    yourNumber1 = int(input("Podaj drugą Liczbę:"))
    yourNumber2 = int(input("Podaj trzecią Liczbę:"))
    yourNumber3 = int(input("Podaj czwartą Liczbę:"))
    yourNumbers = yourNumber, yourNumber1, yourNumber2, yourNumber3
    generatorLiczb = random.choices(liczby, k=4)
    if yourNumbers != generatorLiczb:
        print(f"Twoje liczby to:{yourNumbers}, a wygenerowane to: {generatorLiczb}")
        print("Przegrałeś!")
    else:
        print(f"Twoje liczby to:{yourNumbers}, a wygenerowane to: {generatorLiczb}")
        print("Wygrałeś!")
        break
 
    print("\n")
 