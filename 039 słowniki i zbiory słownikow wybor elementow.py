# słownik słwowników i wybranie jednego z elementów
people1 = {
            'id1': {'name': 'Krzysiek', 'age': 45, 'sex': 'male'},
            'id2': {'name': 'Ania', 'age': 50, 'sex': 'female'}
          }
print("To jest wyświetlenie całego słownika: ", people1)
print()
print("To jest wyświetlenie konkretnego elementu słownika: ", people1['id2'])
print()

# wyświetlenie wartości KLUCZY I WARTOŚCI DLA KLUCZY
for key in people1:
    print(key, people1[key])


# lista słowników - z uwagi na czytelność korzysta sie z nich najczęściej
people2 = [
            {'id': 'qwertyuiop', 'name': 'Krzysiek', 'age': 45, 'sex': 'male'},
            {'id': 'poiuytrewq', 'name': 'Ania', 'age': 50, 'sex': 'female'}
          ]
print("To jest lista słowników: ", people2)
print("To jest pierwszy element (słownik) z listy: ", people2[0])
print()

"""
# słownik z trzema elementami
people3 = {69: 'Anna', 70: 'Chris', 56: 'Krzysiek'}
print(people3[56])


print(people2.pop())
print(people2)
print(people2.pop())
print(people2)
"""
