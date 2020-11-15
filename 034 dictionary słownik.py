# dictionary - słownik KLUCZ - WARTOŚĆ
# nie trzeba zachowywać kolejności, po prostu przypisujemy

pokoje = {}                 # słownik pusty

pokoje = {49: 'Krzysztof Abacki', 69: 'Marek Bebacki'}
print(pokoje)
print(pokoje[69])

pokoje[50] = 'Anna Nowak'           # dodajemy do słownika pod klucz 50 'Anna Nowak' - jeden element
print(pokoje)
print(pokoje.get(49))               # drukujemy klucz 49
pokoje.update({400: "Jasiu Kowalski", 410: "Małgorzata Cebaska"})  # inny sposób dodania, mozna dodać więcej na raz
print(pokoje)
del(pokoje[410])                     # kasujemy wybrany klucz
print(pokoje)
pokoje.pop(49)                      # inny sposób usunięcia
print(pokoje)
pokoje.popitem()                    # usuwa ostatni element
print(pokoje)
print(len(pokoje))                  # zwraca ilość kluczy w słowniku
pokoje.clear()                      # wyczyszczenie słownika
print(pokoje)

a = {'imie': 'Arkadiusz', 'nazwisko': 'Wisniewski'}
print(a['imie'])
print(a['nazwisko'])
