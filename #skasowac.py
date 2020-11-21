ratings1 = {
            "Arkadiusz": (1, 2, 3, 4, 5, 6),
            "Krzysiek": (6, 5, 4, 3, 2, 1)
           }
# wyświetlenie wartośc KLUCZY
for key in ratings1:
    print(key)

# wyświetlenie wartości DLA KLUCZY
for key in ratings1:
    print(ratings1[key])

# wyświetlenie wartości KLUCZY I WARTOŚCI DLA KLUCZY
for key in ratings1:
    print(key, ratings1[key])
