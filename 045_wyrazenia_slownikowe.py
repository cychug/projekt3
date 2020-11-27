# wyrazenia słownikowe TWORZYMY SŁOWNIKI NA PODSTAWIE INNYCH

# tworzymy SŁOWNIK, którego kluczem jest imię a wartością długość imienia
names = {"Krzysiek", "Ania", "Marek", "Karol", "Wojtek"}
nameLenght = {
    name: len(name)
    for name in names
    if name.startswith('A')  # mozemy dodac taki warunek lub nie
}
print(nameLenght)

# tworzymy LISTĘ, którego kluczem będą liczby a wartością potęga tej liczny
numbers = [1, 2, 3, 4, 5, 6, 7]
multipliedNumbers = {
    number: number * number
    for number in numbers
}
print(multipliedNumbers)


# tworzymy SŁOWNIK, którego kluczem będzie stopień C, a wartością stopień F
celcius = [-20, -15, 0, 15, 20]
fahrenheita = {
    stopienF: stopienF * 1.8 + 32
    for stopienF in celcius
}
print(fahrenheita)


# tworzymy SŁOWNIK, którego kluczem będzie nazwa temperatury, a wartością stopień F
celcius = {'t1': -20, 't2': -15, 't3': 0, 't4': 20}
"""
>>> celcius.items()
dict_items([('t1', -20), ('t2', -15), ('t3', 0), ('t4', 20)])
"""
fahrenheita = {
    key: celcius * 1.8 + 32
    for key, celcius in celcius.items()  # stosując .items() tworzymy krotkę w której moemy zapisać dwie wartości klucza i temperatury
    if celcius > -10                        # tak mozemy dodawac kolejne warunki
    if celcius < 20
}
print(fahrenheita)
