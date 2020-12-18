import time


def sumuj_do4(liczba):
    return sum(liczba for liczba in range(1, liczba + 1))


def sumuj_do5(liczba):
    return (1 + liczba) / 2 * liczba


def function_performace(func, argument, how_many_times=1):
    sum = 0
    for i in range(0, how_many_times):  # od 0 do how_many_times
        start = time.perf_counter()
        func(argument)
        end = time.perf_counter()
        sum = sum + (end - start)
    return sum
    

argument = 10000

print(function_performace(sumuj_do4, argument, 5))
print(function_performace(sumuj_do5, argument, 5))
