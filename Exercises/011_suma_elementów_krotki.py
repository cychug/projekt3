
krotka = (2, 4, 6, 8, 2)
lista = [2, 4, 6, 8, 2]
zbior = {2, 4, 6, 8, 2} # elementy zbioru nie mogą się powtarzać !!!


def sum_elements(where):        # na piechotę
    sum = 0
    for i in range(0, len(where)):
        sum = sum + (where[i])
    return sum


def sum_elements1(where):       # z wykorzystaniem sum
    return sum(where)


print(sum_elements(krotka))
print(sum_elements(lista))

print(sum_elements1(krotka))
print(sum_elements1(lista))
print(sum_elements1(zbior))

# print(sum_in_krotka(zbior))
# print(sum_in_krotka(zbior))
