suma = 0
even_number_generator = (item for item in range(6))     # generator tworzy rekord
for item in even_number_generator:                      # dostaenie się do kadego z elementów
    print(item)
    suma = suma + item ** 2
print(suma)

# even_number_generator = (item for item in range(6)) 
for item in even_number_generator:                      # dostaenie się do kadego z elementów
    print("Jeszcze raz", item)
