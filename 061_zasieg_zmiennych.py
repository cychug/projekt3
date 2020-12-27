# nie korzysta się ze zmiennych globalnych w ten sposób. To tylko po to abym wiedział o co chodzi.


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


def add(c, amount=1):
    c = c + amount          # to c jest lokalne, pobieramy 1 + amount też 1
    print(c)                # drukujemy c lokalne czyli 2


c = 1                       # to c jest globalne
add(c)                      # wywoł. fun z c globalnym = 1
print(c)                    # drukujemy c globlane czyli 1
