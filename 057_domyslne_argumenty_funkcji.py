# domyslne argumenty funkcji
# jezeli nie podamy drugiego argumentu funckcji to przyjmie on wartość podaną za = 

def increment(x, amount = 1):
    return x + amount


print(increment(1, 100))    # tu są podane oba argumenty
print(increment(1))         # tu nie ma drugiego argumentu ale pierwszy jest, drugi przyjmie wartość domyslna
