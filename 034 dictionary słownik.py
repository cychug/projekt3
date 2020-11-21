# dictionary - słownik KLUCZ - WARTOŚĆ
# nie trzeba zachowywać kolejności, po prostu przypisujemy
# kluczem mogą być te nazwy: 'imie1'

pokoje = {}                 # słownik pusty
pokoje = {49: 'Krzysztof Abacki', 69: 'Marek Bebacki'}
print("Wszystkie pokoje", pokoje)
print("W pokoju 69 jest:", pokoje[69])

oceny = {                               # słownik krotek
          'Arkadiusz': (1, 2, 3, 5, 4, 3),
          'Krzysiek': (3, 4, 3, 6, 6, 2, 1, 5, 4)
        }

print("Oceny Arkadiusza", oceny['Arkadiusz'])               # wydrukje element (krotkę) ze słownika - oceny Arkadiusza

pokoje[50] = 'Anna Nowak'           # dodajemy do słownika pod klucz 50 'Anna Nowak' - jeden element
print(pokoje)
print(pokoje.get(49))               # wyświetlamy klucz 49

pokoje.update({400: "Jasiu Kowalski", 410: "Małgorzata Cebaska"})  # inny sposób dodania, mozna dodać więcej na raz
print("Wszystkie pokoje po dodaniu dwóch: ", pokoje)

del(pokoje[410])                     # kasujemy wybrany klucz
print("Po skasowaniu pokoju 410: ", pokoje)

pokoje.pop(49)                      # inny sposób usunięcia
print(pokoje)
pokoje.popitem()                    # usuwa ostatni element
print(pokoje)
print(len(pokoje))                  # zwraca ilość kluczy w słowniku
pokoje.clear()                      # wyczyszczenie słownika
print(pokoje)

"""
a = {'imie': 'Arkadiusz', 'nazwisko': 'Wisniewski'}  # zbiór słownika
print(a['imie'])
print(a['nazwisko'])
"""
