"""
break to przerwanie pętli i wyście
continue przerywamy od tego momentu i wracamy, następne nie zostaną wykonane ale tylko w tym jednym przejściu
"""
wynik = 0
for i in range(3):
    x = int(input("Podaj liczbę dodatnią:"))
    if (x > 0):
        wynik += x
    else:
        print("Miała być liczba większa od zera. Przerywam całkowicie działanie.")
        break     # przerywamy działąnie pętli i wychodzimy z niej
print("Wynik dodawania liczb:", wynik)
