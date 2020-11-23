wybor = input("Podaj działanie: * mnozenie, / dzielenie, + dodawanie, - odejmowanie, ^ potęgowanie, % modulo : ")
a = int(input("Podaj liczbę a: "))
b = int(input("Podaj liczbę b: "))
print("a =", a, "b =", b, "działanie: ", wybor)
if (wybor == "*"):
    print(a, "*", b, "=", a * b)
elif (wybor == "/"):
    if (b == 0):
        print("Cholero nie dziel przez 0")
    else:
        print(a, "/", b, "=", a / b)
elif (wybor == "+"):
    print(a, "+", b, "=", a + b)
elif (wybor == "-"):
    print(a, "-", b, "=", a - b)
elif (wybor == "^"):
    print(a, "^", b, "=", a**b)
elif (wybor == "%"):
    print(a, "%", b, "=", a % b)        # reszta z dzielenia
else:
    print("Twój wybór był nieprawidłowy")
