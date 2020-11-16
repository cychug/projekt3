x = 0                           # wypisanie liczb parzystych od 1 do 100
for i in range(100):
    x = x + 1
    if (x % 2 == 0):
        print(x)

x = 0
for i in range(100):            # wypisanie liczb parzystych od 0 do 99
    if (x % 2 == 0):
        print(x)
    x = x + 1
