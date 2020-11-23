liczba = int(input("Podaj dowolną liczbę: "))
print("Podałeś liczbę:", liczba)
if (liczba >= 0):
    print(liczba)
elif (liczba < 0):
    liczbaBezwzgledna = abs(liczba)
    print("Liczba bezwzględna z", liczba, "to:", liczbaBezwzgledna)
