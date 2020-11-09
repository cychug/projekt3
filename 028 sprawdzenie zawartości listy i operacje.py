# in
# not in
# operacje na listach

imiona = ["Krzysiek", "Ania", "Bartek", "Kuba", "Robert"]
liczby = [2, 1, 45, 100]
mieszane = [1, "as", 52, "k"]
# print("Krzysiek" in imiona)
if "Krzysiek" in imiona:
    print("Cześć Krzysiek")
else:
    print("Krzyśka nie ma w zbiorze")

if (2 not in liczby):
    print("W zbiorze nie ma liczny 2")
else:
    print("2 jest w zbiorze")
print(4 * imiona)           # lista zostanie wyświetlona 4 razy
print([8, 7] + liczby)      # dodanie listy do listy (chwilowe)
print(liczby)
liczby = [8, 7] + liczby    # przypisanie do zmiennej
print(liczby)
