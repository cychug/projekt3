# funkcje anonimowe, lambda


def duble(x):
    return x * 2


print(duble(4))

# tak można to wywołać (1)
test = lambda x: x * 2
print(test(4))

# tak też można wywyłać
print((lambda x: x * 2)(4))

# to jest przykład zastosowania lambda
my_list = [2, 14, 13, 17, 22]
# tworzymy listę przefiltrowaną i zostają tylko elementy parzyste; poniżej składnia lambda
my_list_filtered = list(filter(lambda x: x % 2 == 0, my_list))
print(my_list_filtered)

# to jest inny niż lambda sposób - lista wyrażeniowa
my_list_filtered = [x for x in my_list if (x % 2 ==0)]
print("Przy pomocy wyrażenia: ",my_list_filtered)


# to jest tradycyjny sposób przefiltrowania


def przefiltruj_liste(x):
    new_list = []
    for a in x:
        if (a % 2) == 0:
            new_list.append(a)
    return new_list


print(przefiltruj_liste(my_list))


# dodanie do listy elementów drugiej listy 1 sposób
a = ["apple", "banana", "cherry"]
b = ["Ford", "BMW", "Volvo"]

for x in b:
    a.append(x)

print(a)

# prościej przy pomocy .extend()
a = ["apple", "banana", "cherry"]
b = ["Ford", "BMW", "Volvo"]
a.extend(b)
print(a)

# przy pomocy +
a = ["apple", "banana", "cherry"]
b = ["Ford", "BMW", "Volvo"]
print(a + b)
"""
append(): append the object to the end of the list.
insert(): inserts the object before the given index.
extend(): extends the list by appending elements from the iterable.
List Concatenation: We can use + operator to concatenate multiple lists and create a new list.
"""