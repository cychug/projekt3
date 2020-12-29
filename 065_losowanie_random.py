"""
random - losowy
random()        0<= x < 1 lub [0,1)

uniform(2.5, 10.0)      2.5 <= x < 10.0 [2.5, 10)
randrange(10)           z puli od (0...9)
ranndrange(0, 15, 2)    parzyste z puli (0,2,4, ...14) - bo daliśmy step = 2   
randint(0, 4)           [0,1,2,3,4] - to najlepsze
"""

import random

for x in range(10):         # przjdzie przez 10 elementów od x = 0 do 9
    print(x, random.random())

print("\n")

for x in range(10):
    print(x, random.uniform(0, 100))

print("\n")

for x in range(10):
    print(x, random.randint(0, 4))



# przykład programu
"""
strzelam 100 razy jakie jest prawdopodobieństwo trafienia


hit_numbers = int(input("Podaj ilość strzałów: "))
print(hit_numbers)
hit = 0
no_hit = 0
for x in range(hit_numbers):
    chance = random.uniform(0, 100)
    if (chance > 50):
        hit = hit + 1
    else:
        no_hit = no_hit + 1
print("hit: %", hit / hit_numbers * 100, "no_hit: %", no_hit / hit_numbers * 100)
"""


def hit_persentage(hit_numbers):
    hit = 0
    no_hit = 0
    for x in range(hit_numbers):
        chance = random.uniform(0, 100)
        if (chance > 50):
            hit = hit + 1
        else:
            no_hit = no_hit + 1
    return hit / hit_numbers * 100, no_hit / hit_numbers * 100


hit_numbers = int(input("Podaj ilość strzałów: "))
(a, b) = hit_persentage(hit_numbers)
print("Hit: %", a, "No hit: %", b)
