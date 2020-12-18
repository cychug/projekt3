# mierzenie wydajności programu
# licznik wydajności, zwraca wartość do mierzenia krótkich odcinków czasu

import time


# obliczenie sumy przy pomocy pętli


def sumuj_do1(a):
    suma = 0
    for i in range(1, a + 1):
        suma = suma + i
    return suma


# GENERATOR listy


def sumuj_do2(liczba):
    return sum([liczba for liczba in range(1, liczba + 1)])


# GENERATOR ZBIORU


def sumuj_do3(liczba):
    return sum({liczba for liczba in range(1, liczba + 1)})


# GENERATOR


def sumuj_do4(liczba):
    return sum(liczba for liczba in range(1, liczba + 1))


# CIĄG ARYTMENTYCZNY - SUMA KOLEJNYCH LICZB: (1 + 5) / 2 * 5
# suma pierwszej i ostatniej w ciągu / przez 2 8 ostatnia
# Suma kolejnych liczb: 1, 2, 3, 4, 5 = [(1 + 5) / 2 * 5 (ilość liczb) = 15


def sumuj_do5(liczba):
    return (1 + liczba) / 2 * liczba


# tu się dzieje magia wywołania funkcji przez funkcję z argumentem

def function_performace(func, argument):
    start = time.perf_counter()
    func(argument)
    end = time.perf_counter()
    return end - start


argument = 10000

print(function_performace(sumuj_do1, argument))
print(function_performace(sumuj_do2, argument))
print(function_performace(sumuj_do3, argument))
print(function_performace(sumuj_do4, argument))
print(function_performace(sumuj_do5, argument))
