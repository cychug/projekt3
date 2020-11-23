
# WYŚWIETLENIE WARTOŚCI SŁOWNIKÓW ZE ZBIORU
ratings1 = {
            "Arkadiusz": (1, 2, 3, 4, 5, 6),
            "Krzysiek": (6, 5, 4, 3, 2, 1)
           }
# wyświetlenie wartośc KLUCZY
for key in ratings1:
    print(key)

# wyświetlenie wartości DLA KLUCZY
for key in ratings1:
    print(ratings1[key])

# wyświetlenie wartości KLUCZY I WARTOŚCI DLA KLUCZY
for key in ratings1:
    print(key, ratings1[key])


# WYŚWIETLENIE WARTOŚCI LISTY
people3 = [
            "Krzysiek",
            "Ania",
            "Ola"
          ]

for imie in people3:
    print(imie)

# WYŚWIETLENIE WARTOŚCI SŁOWNIKAÓW Z LISTY SŁOWNIKÓW
people2 = [
            {'id': 'qwertyuiop', 'name': 'Krzysiek', 'age': 45, 'sex': 'male'},
            {'id': 'poiuytrewq', 'name': 'Ania', 'age': 50, 'sex': 'female'}
          ]

for record in people2:              # dla kadego rekordu (który jest słownikiem) w liscie peopple2 wykonaj pętlę poniej
    for key in record:              # dla kadego klucza w rekordzie
        print(key, record[key])     # wypisz nazwę klucza oraz jego wartość

# WYŚWIETLENIE WARTOŚCI SŁOWNIKAÓW ZE ZBIORU SŁOWNIKÓW
people1 = {
            'id1': {'name': 'Krzysiek', 'age': 45, 'sex': 'male'},
            'id2': {'name': 'Ania', 'age': 50, 'sex': 'female'}
          }
for key in people1:
    print(key)
    for secondaryKey in people1[key]:
        print(secondaryKey, people1[key][secondaryKey])

# WYŚWIETLENIE WARTOŚCI SŁOWNIKÓW ZE ZBIORU - LEPSZE I SZYBSZE (WG. PRAKTYWÓW
print("######### lepszy sposób #########")
people1 = {
            'id1': {'name': 'Krzysiek', 'age': 45, 'sex': 'male'},
            'id2': {'name': 'Ania', 'age': 50, 'sex': 'female'}
          }
for id, dictionary in people1.items():      # zastosowanie .items()
    print("ID", id)
    for key in dictionary:
        print(key, ":", dictionary[key])


print(people1.items())          # wyświetli całą zawartość
