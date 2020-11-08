wartosc = int(input("Sprawdzę, czy liczba jest z zakresu (1,10). Podaj liczbę: "))

if (wartosc > 1 and wartosc < 10):
    print("Wartość naley do (1,10)")
else:
    print("Wartość", wartosc, "jest spoza zakresu (1,10).")
input("Coś kliknij")            # na chwilę zatrzymuję program aby zobaczyć co i jak
print("Teraz sprawdzę, czy a = 5 lub b = 2")
a = int(input("Podaj wartość a: "))
b = int(input("Podaj wartość b: "))
if (a == 5 or b == 2):
    print("a = 5 lub b = 2")
if (not(a == 5 or b == 3)):
    print("a nie jest równe 5 lub b nie jest równe 3")

"""
and "i"  True and True = True; True and False = False; False and False = False - KONIUNKCJA
or "lub" True or True = True, True or False = True, False or False = False - ALTERNATYWA
not "zaprzeczenie" -> np.: coś NIE JEST w zakresie od 1 do 10...
"""
