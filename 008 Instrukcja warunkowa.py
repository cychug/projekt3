"""
JESLI (PRAWDA)
    TO...
JESLI COS INNEGO (PRAWDA)
    TO...
A CAŁKOWICIE W INNYM WYPADKU
    TO...

 elif od ang else if
"""
a = int(input("Podaj liczbę a: "))
b = int(input("Podaj liczbę b: "))
print("a =", a, "b =", b)
if (a > b):                             # ważny jest dwukropek
    print(a, "jest większe od", b)        # wazne jest wcięcie
elif (b > a):
    print(b, "jest większe od", a)
else:
    print("a jest równe b")
