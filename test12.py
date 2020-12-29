import random

for x in range(10):         # przjdzie przez 10 elementów od x = 0 do 9
    print(x, random.random())

print("\n")

for x in range(10):
    print(x, random.uniform(0, 100))

print("\n")

for x in range(10):
    print(x, random.randint(0, 4))

