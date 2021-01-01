import random


def will_weapon_hit(weaponChanceToHitPercentage):
    isHitChance = random.uniform(0,100)
    if (isHitChance < weaponChanceToHitPercentage):
        return "hit"
    else:
        return "not hit"


x = 0
listHit = []

while x < 100:
    x = x + 1
    listHit.append(will_weapon_hit(50))

print(listHit)

from collections import Counter

"""
Dict subclass for counting hashable items. 
Sometimes called a bag or multiset.
Elements are stored as dictionary keys and their counts are stored as dictionary values.

>>> c = Counter('abcdeabcdabcaba')  # count elements from a string
>>> c.most_common(3)                # three most common elements
[('a', 5), ('b', 4), ('c', 3)]
>>> sorted(c)                       # list all unique elements
['a', 'b', 'c', 'd', 'e']
>>> ''.join(sorted(c.elements()))   # list elements with repetitions
'aaaaabbbbcccdde'
>>> sum(c.values())                 # total of all counts
15
"""

dictionaryHit = Counter(listHit)
print(dictionaryHit)

"""
x = 0


while x < 100:
    x = x + 1
    print(random.randint(0,10))

"""