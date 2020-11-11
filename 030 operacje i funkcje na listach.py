# len() - długość, ile jest elementów w liście, to jest funkcja
# .append - pozwala dodawać elementy do końca listy
# .extend - rozszerzamy listę o element(y) drugiej listy
# .insert - wstawić
# .index() - zwraca numer pozycji tzw. indeks pierwszego wystąpienia UWAGA: liczy od 0
# .sort(reverse=False) - sortuj rosnąco .sort()
# max() - maksymalny element
# min() - minimalny element
# .count - ile razy coś wystąpiło
# .pop - "trzaśnij" usuń ostatni element, .pop() usuwa ostatni element
# .remove - usunie pierwszy napotakny takie element
# .clear() - wyczyść listę, usunięcie wszystkich elementów (musi być pusty nawias lista1.clear()
# .reverse - odwrotna kolejność (bez sortowania!)

lista1 = [54, 1, -2, 20, 1]
lista2 = [62, 1, 12, 12, 0]
lista3 = [62, 1, 12, 12, 0]
lista4 = ["Arkadiusz", "Wioletta", "Marek", "Basia"]
print("Lista 1:", lista1)
print("Długość listy:", len(lista1))
lista1 = lista1 + [4] + [5]     # to jest dodanie do listy, nie jest to najlepsze rozwiązanie
print("Lista rozszerzona o dwa elementy: ", lista1)
lista1.append(4)                # dodajemy jeden element optymalnie
print("Lista z dodanym jeszcze jednym elementem lepiej:)", lista1)
print("Do listy ", lista2, "dodamy kolejną listę - wyjdzie lista w liście")
lista2.append([2, 12, 24, 2])   # monza dodać do listy listę ale przez append wyjdzie lista w liście
print(lista2)
print("a tu rozszerzamy listę", lista3, " o elementy/drugąlistę")
lista3.extend([2, 12, 24, 2])   # rozszerzamy listę o elementy drugiej listy
print(lista3)
print("Wsadzimy na pierszą pozycję listy", lista4, " Krzyska")
lista4.insert(0, "Krzysiek")    # wsadzenie elementu na daną pozycję listy 0 - pierwsza
print(lista4)
print("To jest lista1", lista1)
print("Oto na jakiej pozycji tej listy jest element 20:", lista1.index(20))
print("To jest lista1", lista1)
lista1.sort()                   # sortujemy rosnąco
print("To jest lista1 posortowana rosnąco", lista1)
lista1.sort(reverse=True)       # sortujemy malejąco
print("To jest lista1 posortowana malejąco", lista1)
print(min(lista1))
print("Maksymalny element listy", lista1, max(lista1))  # maksymalny element listy
print("Minimalny element listy", lista1, min(lista1))   # minimalny element listy
print("Element 1 wystąpił w liście:", lista1, lista1.count(1), "razy")  # liczymy ile razy wystąpił
print("Oto lista1", lista1, "z której usunę ostatni element.")
lista1.pop()
print(lista1)
print("Teraz usunę z listy pierwszy napotkany element 5")
lista1.remove(5)
print(lista1)
print("Czyszczę listę1")
lista1.clear()
print("Teraz lista4 po czyszczeniu", lista1)
print("Lista4 wygląda tak:", lista4)
print("teraz odwracamy kolejność elementów listy4")
lista4.reverse()
print(lista4)

#zmieniłem