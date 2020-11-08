"""
break to przerwanie pętli i wyście
continue przerywamy od tego momentu i wracamy, następne nie zostaną wykonane ale tylko w tym jednym przejściu
"""
wynik = 0
i = 0
while i < 3:
    x = int(input("Podaj liczbę dodatnią:"))
    if (x > 0):
        wynik += x
    else:
        print("Miała być liczba dodatnia")
        continue                # jezeli była ujemne to przerywamy (nie idzie niej) i wraca do góry while
    print("Aktualny wynik dodawania liczb dodatnich to:", wynik)
    i += 1
