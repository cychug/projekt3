# lista

countries = ['Polska', 'Niemcy', 'Grecja', 'Szwecja', 'Rosja']

for i, country in enumerate(countries):
    print(i, country)

# tupla
countries = ('Polska', 'Niemcy', 'Grecja', 'Szwecja', 'Rosja')

for i, country in enumerate(countries):
    print(i, country)

# struktury złozone - 
persons = [('Dawid', 25), ('Jan', 23), ('Marcin', 22)]

for i, person in enumerate(persons):
    print(i, ":", person)

# Możemy też rozpakować obiekty i to wszystko połączyć z enumerate. Będzie to wymagać małego zabiegu ale da się
persons = [('Dawid', 25), ('Jan', 23), ('Marcin', 22)]

for i, (name, age) in enumerate(persons):
    print(i, ".", name, 'age', age)
