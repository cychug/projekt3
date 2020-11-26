name = "krzysiek"
name1 = "ANIA"
print(len(name))    # funkcja

# METODY
print(name.capitalize())    # pierwsza litera bedzie zmieniona na wielka
print(name.upper())         # wszystkie litery zmienione na wielkie
print(name1.lower())        # wszysktie na małe

print(name[0])              # pierwsza litera
print(name[-1])             # ostatnia litera
print(name[0:2])            # pierwsze dwie lietry
print(name[3:])             # od trzeciej włącznie litery do KOŃCA
print(name[:-3])            # od początku do -3
print(name[-3:])            # od -3 do do końca

channel = "Jak napisać ksiązkę"
print(channel.split(" "))   # utworzy listę z wyrazami podzielonymi spacją

join_string = " "           # czym połączymy, w tym przypadku spacją
print(join_string.join(['Jak', 'napisać', 'ksiązkę.']))     # metoda .join
print(name.startswith("K"))    # sprawdzenie czy string zaczyna się literą, wielkość ma znaczenie
print(name.startswith("k"))

print(name.endswith("k"))       # sprawdzenie czy string kończy się literą, wielkość ma znaczenie

print(name.rstrip("k"))         # usunięcie z prawej strony litery k (tylko na brzegach)
print(name.lstrip("k"))         # usunięcie z lewej strony litery k (tylko na brzegach)

print(name.strip("k"))         # usunięcie z prawej i lewej strony litery k (tylko na brzegach)
