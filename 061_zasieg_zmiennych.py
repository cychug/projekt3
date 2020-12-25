def add():
    c = 5   # zakres zmiennej c jest lokalny, tylko w obrębie tej funkcji
    print(c)
    return c    # to zwraca 5 a nie c


add()

c = 5   # to jest zmienna globalna;


def add1():
    global c    # tu pobieramy zmienną globalną do funkcji
    c = c + 5   # zakres zmiennej c jest lokalny, tylko w obrębie tej funkcji
    print(c)


add1()
