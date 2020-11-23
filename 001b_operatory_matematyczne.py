a = 4
b = 2
c = 4.0         # zmienno przecinkowa float
d = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % d)        # dzielenie z resztą

print(type(a + b))
print(type(a / b))
print(type(a / c))  # działanie przy jednej liczbie int i drugiej float da wynik float

a = 5
a += 2              # -= *= /=
print(a)
