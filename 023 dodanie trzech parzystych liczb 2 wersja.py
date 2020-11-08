wynik = 0
i = 0
while i < 3:
    x = int(input("Podaj dowolną liczbę:"))
    parzysta = x % 2
    if (x <= 0) or (parzysta != 0):
        continue
    wynik += x
    i += 1
print("Wynik dodawania:", wynik)
