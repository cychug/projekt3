"""
    Argmumenty kluczowe i pozycjne
    kluczowy - w postaci: klucz - wartość (domyślny)
    pozycyjny - takich, których liczy się kolejność przy wywołaniu
"""


def greet(name, message="Hello", separator=" "):    # tu pierwszy jest wymagan, 2 i 3 nie bo mają wartości domyślne
    print(message, name, sep=separator)


greet("Arek", "Cześć")                  # wyświetli: Cześć Arek TU SĄ TYLKO ARGUMENTY POZYCYJNE
greet(message="Cześć", name="Arek")     # TU SĄ ARGUMENTY KLUCZOWE ZAMIENIONE MIEJSCAMI

print("Hellow", "World", sep="!!!")     # wyświetli Hellow!!!World, sep - jest argumentem standardowym i mozna go wykorzystywać

greet("Marek", "Cześć", "\n")           # wyswietli: Cześć ENTER Marek; jak nie wpiszę "\n" to przyjmie wartość domyślną " "
greet("Marek", "Cześć", "***")          # wyswietli: Cześć***Marek

# mozemy tez zamieniac kolejnosc argumentow z kluczem
greet("Marek", "\n")
greet("Marek")