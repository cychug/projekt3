# określenie czasu ile trwa sprawdzenie czy dany argument jest w liscie a ile w zbiorze
# sprawdzenie w zbiorze jest o wiele szybsze !!!!!
# Jezeli jest *arg to są to argumenty NIENAZWANE (krotka?)
# Jezeli jest **arg to są to argumenty NAZWANE (słownik?)

import time


def check_container(element, where):
    if element in where:
        return True
    else:
        return False


# do tej funkcji przesyłamy pod *arg wiele argumentów; *arg najlepiej wymienić na końcu
def function_performace(func, how_many_times=1, *arg):
    sum = 0
    print(arg[0])   # to wyświetli co jest pod 1 argumentem
    print(arg[1])   # to wyświetli co jest pod 2 argumentem
    print(how_many_times)
    for i in range(0, how_many_times):  # od 0 do how_many_times
        start = time.perf_counter()
        func(*arg)
        end = time.perf_counter()
        sum = sum + (end - start)
    return sum


elements_number = int(input("Podaj ilość elementów: "))
element = int(input("Podaj wartość szukanego elementu: "))
how_many_times = int(input("Podaj ilość powtórzeń: "))

lista = [numbers for numbers in range(1, elements_number)]
zbior = {numbers for numbers in range(1, elements_number)}
krotka = tuple(range(elements_number))

print("Czas wyszukania z listy: ", function_performace(check_container, how_many_times, element, lista))
print("Czas wyszukania ze zbioru: ", function_performace(check_container, how_many_times, element, zbior))
print("Czas wyszukania ze zbioru: ", function_performace(check_container, how_many_times, element, krotka))