wynik = 0
i = 0
while i < 3:
    x = int(input("Podaj dowolną liczbę:"))
    if (x > 0) and (x % 2 == 0):
        wynik += x
        i += 1
    continue
print("Wynik dodawania:", wynik)
