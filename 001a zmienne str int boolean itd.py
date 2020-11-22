# TRZY sposoby na zainicjalizowanie str
name = "Kamil \n\n channel"
name1 = 'Kamil\'s'       # wstawiamy \ aby podac '
name2 = """Kamil


chanell
"""
print(name)
print(name1)
print(name2)

# zmienne liczbowe
a = 10
b = 2.5
print(a + b)           # python sam skonwertował
c = 1_000_000          # dzue liczby
print(c)

# zmienne boolean
is_sky_blue = True
is_sun_blue = False
print(is_sky_blue)

# sprawdzenie typu zmiennej
print(type(name))
print(type(a))
print(type(is_sky_blue))

# konwersje zmiennych
first = 2
second = "3"
print(first + int(second))  # zamiana ze str na int
print(str(first) + second)  # zamiana int na str

