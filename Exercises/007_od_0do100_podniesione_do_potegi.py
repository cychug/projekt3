
suma = 0
number_generator = (element for element in range(101))
# print("Suma liczb parzystych: ", sum(number_generator))
for element in number_generator:
    print("Element: ", element)
    suma = suma + element ** 2
print("Suma: ", suma)
# print("Suma liczb parzystych: ", sum(number_generator))       # suma liczb parzystych - od razu BEZ ZAJ

"""
number_generator = (element for element in range(100) if (element % 2 == 0))
print("Suma liczb parzystych: ", sum(number_generator))       # suma liczb parzystych - od razu BEZ ZAJ
"""
