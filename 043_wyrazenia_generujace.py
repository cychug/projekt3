# wyrazenie generujące w () A NIE W []
# zajmuje bardzo mało miejsca w pamieci
# taki będzie efekt: <generator object <genexpr> at 0x7f9158de0f90>
# generator słuzy do wypisania elemntów ale ich niezapamiętywania
# potrzebny przy duych ilościach danych
import sys

even_number_generator = (element for element in range(40) if (element % 2 == 0))
print("generator: ", even_number_generator)                     # wypisze wszystkie liczny parzyste
print("Suma liczb parzystych: ", sum(even_number_generator))    # suma liczb parzystych - od razu BEZ ZAJMOWANIA DODATKOWEJ PAMIĘCI

for item in even_number_generator:      # dostaenie się do kadego z elementów
    print(item)

# stary sposób w []
even_number = [element for element in range(40) if (element % 2 == 0)]
print("Stary sposób: ", even_number)

print("Zajęctość pamięci even_number_generator TEN SUPER POMYSŁ : ", sys.getsizeof(even_number_generator))     # ile miejsca - mniej
print("Zajęctość pamięci even_numebR LISTA: ", sys.getsizeof(even_number))                          # ile miejsa
