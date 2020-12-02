
def dzielenie(a, b):
    if (b == 0):
        return "Nie dziel przez 0"
    return(a / b)

print(dzielenie(2, 0))


def dzielenie(a, b):
    if (b == 0):
        return      # jak będzie = 0, to wychodzimy z tej funkcji bez niczego "None" = True
    return(a / b)

print(dzielenie(2, 0))


# teraz wykorzystamy wyjsice z funcki przy probie dzielenie przez 0 - zostanie zwrócona wartość None, która = FALSE


def dzielenie(a, b):
    if (b == 0):
        return      # zwaraca None = False
    return(a / b)


x = dzielenie(10, 10)
if (x):
    print("Podzielono poprawnie: ", x)
else:
    print("Cholero nie dziel przez 0")
