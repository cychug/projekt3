"""
obiekt to zmienna, która ma więcej możliwości,
można wywołać na nim funkcje
może mieć więcej niż 1 wartość

obiekt immutable: bool, int, float, tuble, str

immutable - niezmienne
mutable - zmienne
"""
a = 4       # a jest obiektem typu int i jest niezmenny immutable
print(a.bit_length())

listSample = [1, 4, 512, 24]
listSample2 = listSample    # ta lista jest zmienna (mutable) w tym miejscu przypisujemy dokładnie adres miejsca przechowywania a nie wartości
listSample2.append(465)
print(listSample)
print(listSample2)
print("Adres listSample:  ", id(listSample))
print("Adres listSample2: ", id(listSample2)) # oba adresy będą takie same!

a = 4
b = a
b = 7
print("a=", a, "b=", b) # a= 4, b = 7 # tu zadziała to inaczej, ponieważ to jest przypisanie adresu wartości


listSample = [1, 4, 512, 24]
listSample2 = listSample
listSample2 = [2]
print(listSample)
print(listSample2)
print("Adres listSample:  ", id(listSample))
print("Adres listSample2: ", id(listSample2))

k = 4
h = 4
print(id(k))    # adres będzie taki sam dla k i h o ile ich wartość będzie taka sama
print(id(h))


# zmienna globalna c = 5, ale w funkcji jest też taka sama nazwa lokalnie.
c = 5
def add(c, amount=1):
    c = c + amount
    return c


print(add(c))
print(c)


def append_element_to_list(list1, element):
    print(id(list1))
    list1.append(element)
    print(id(list1))
    return list1


lista = [1, 2, 3, 4]
print(append_element_to_list(lista, 5))
